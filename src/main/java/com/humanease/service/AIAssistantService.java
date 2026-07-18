package com.humanease.service;

import com.humanease.entity.Medicine;

public interface AIAssistantService {
    
    /**
     * Generates a complete Medicine object for an unknown medicine using AI.
     */
    Medicine generateMedicineInfo(String medicineName);

    /**
     * Answers follow-up questions regarding a specific medicine.
     */
    String answerFollowUpQuestion(String medicineName, String question);

    /**
     * Checks interactions between multiple medicines.
     */
    String checkInteractions(String[] medicineNames);

    /**
     * Analyzes a prescription image and extracts medicines and interactions.
     */
    String analyzePrescription(org.springframework.web.multipart.MultipartFile image);
}
