package com.humanease.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.humanease.entity.Medicine;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class GeminiAIServiceImpl implements AIAssistantService {

    @Value("${gemini.api.key:YOUR_API_KEY_HERE}")
    private String apiKey;

    @Value("${gemini.api.url:https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent}")
    private String apiUrl;

    private final RestTemplate restTemplate = new RestTemplate();
    private final ObjectMapper objectMapper = new ObjectMapper();

    private String callGeminiAPI(String prompt) {
        int maxRetries = 3;
        int attempt = 0;
        
        while (attempt < maxRetries) {
            try {
                HttpHeaders headers = new HttpHeaders();
                headers.setContentType(MediaType.APPLICATION_JSON);

                Map<String, Object> requestBody = new HashMap<>();
                requestBody.put("contents", List.of(
                        Map.of("parts", List.of(
                                Map.of("text", prompt)
                        ))
                ));

                HttpEntity<Map<String, Object>> request = new HttpEntity<>(requestBody, headers);
                String urlWithKey = apiUrl + "?key=" + apiKey;

                String response = restTemplate.postForObject(urlWithKey, request, String.class);
                JsonNode root = objectMapper.readTree(response);
                
                return root.path("candidates").get(0).path("content").path("parts").get(0).path("text").asText();
            } catch (org.springframework.web.client.HttpStatusCodeException e) {
                String errorBody = e.getResponseBodyAsString();
                int statusCode = e.getStatusCode().value();
                
                // Google APIs sometimes return 500 HTTP code but 503 inside the JSON, or 429 for rate limits
                if (statusCode >= 500 || statusCode == 429 || errorBody.contains("\"code\": 503") || errorBody.contains("high demand")) {
                    attempt++;
                    if (attempt >= maxRetries) {
                        System.err.println("Gemini API Error (Retry Exhausted): " + errorBody);
                        return "AI Analysis Error: Service is currently experiencing extremely high demand. Please try again later.";
                    }
                    System.out.println("Gemini API High Demand/Server Error. Retrying attempt " + attempt + " in 2 seconds...");
                    try { Thread.sleep(2000); } catch (InterruptedException ie) { Thread.currentThread().interrupt(); }
                } else {
                    System.err.println("Gemini API Error: " + errorBody);
                    return "AI Analysis Error: " + errorBody;
                }
            } catch (Exception e) {
                System.err.println("Gemini API Error: " + e.getMessage());
                return "AI Analysis is currently unavailable. Error: " + e.getMessage();
            }
        }
        return "AI Analysis failed after retries.";
    }

    @Override
    public Medicine generateMedicineInfo(String medicineName) {
        String prompt = "You are a medical AI assistant. Provide a highly detailed summary for the medicine '" + medicineName + "'. " +
                "Return the response in a structured format suitable for parsing, including Generic Name, Category, Uses, Dosage, Side Effects, Food Warnings, Pregnancy Safety, and Interactions.";
        
        String aiResponse = callGeminiAPI(prompt);
        
        // Basic parsing (In a real scenario, we'd ask Gemini to return strict JSON and parse it)
        Medicine med = new Medicine();
        med.setMedicineName(medicineName);
        med.setDescription("AI Generated Summary: " + aiResponse);
        med.setCategory("AI Analyzed");
        return med;
    }

    @Override
    public String answerFollowUpQuestion(String medicineName, String question) {
        String prompt = "You are a medical expert. The user is asking about the medicine '" + medicineName + "'. " +
                "Question: '" + question + "'. Provide a safe, clear, and medically accurate response.";
        return callGeminiAPI(prompt);
    }

    @Override
    public String checkInteractions(String[] medicineNames) {
        String meds = String.join(", ", medicineNames);
        String prompt = "You are a clinical pharmacologist. Check for drug interactions between the following medicines: " + meds + ". " +
                "Categorize the interaction as 'Safe', 'Moderate', or 'Dangerous'. Explain why and provide medical warnings.";
        return callGeminiAPI(prompt);
    }

    private String callGeminiVisionAPI(String prompt, org.springframework.web.multipart.MultipartFile image) {
        int maxRetries = 3;
        int attempt = 0;
        
        while (attempt < maxRetries) {
            try {
                HttpHeaders headers = new HttpHeaders();
                headers.setContentType(MediaType.APPLICATION_JSON);

                byte[] imageBytes = image.getBytes();
                String base64Image = java.util.Base64.getEncoder().encodeToString(imageBytes);
                String mimeType = image.getContentType();
                if (mimeType == null || !mimeType.startsWith("image/")) {
                    mimeType = "image/jpeg";
                }

                Map<String, Object> inlineData = new HashMap<>();
                inlineData.put("mimeType", mimeType);
                inlineData.put("data", base64Image);

                Map<String, Object> imagePart = new HashMap<>();
                imagePart.put("inlineData", inlineData);

                Map<String, Object> textPart = new HashMap<>();
                textPart.put("text", prompt);

                Map<String, Object> requestBody = new HashMap<>();
                requestBody.put("contents", List.of(
                        Map.of("parts", List.of(textPart, imagePart))
                ));

                HttpEntity<Map<String, Object>> request = new HttpEntity<>(requestBody, headers);
                String urlWithKey = apiUrl + "?key=" + apiKey;

                String response = restTemplate.postForObject(urlWithKey, request, String.class);
                JsonNode root = objectMapper.readTree(response);
                
                return root.path("candidates").get(0).path("content").path("parts").get(0).path("text").asText();
            } catch (org.springframework.web.client.HttpStatusCodeException e) {
                attempt++;
                if (attempt >= maxRetries) {
                    return "AI Vision Error: " + e.getResponseBodyAsString();
                }
                try { Thread.sleep(2000); } catch (InterruptedException ie) { Thread.currentThread().interrupt(); }
            } catch (Exception e) {
                return "AI Vision Error: " + e.getMessage();
            }
        }
        return "AI Vision Analysis failed.";
    }

    @Override
    public String analyzePrescription(org.springframework.web.multipart.MultipartFile image) {
        String prompt = "You are a medical AI. Carefully read the uploaded prescription image. " +
                        "1. Extract the names of all the medicines written on it. " +
                        "2. Briefly explain what each medicine is used for. " +
                        "3. Most importantly, flag any dangerous interactions between these medicines. " +
                        "Return the result in clear, formatted HTML (using <ul>, <li>, <strong>, <br> tags). Do not use markdown backticks.";
        return callGeminiVisionAPI(prompt, image);
    }
}
