package com.humanease.controller;

import com.humanease.service.OCRService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import java.util.Map;

@Controller
public class OCRController {

    @Autowired
    private OCRService ocrService;

    @GetMapping("/scanner")
    public String scannerPage() {
        return "prescription_scanner";
    }

    @PostMapping("/api/ocr/scan")
    @ResponseBody
    public ResponseEntity<?> scanPrescription(@RequestParam("file") MultipartFile file) {
        if (file.isEmpty()) {
            return ResponseEntity.badRequest().body("Please upload a file");
        }
        try {
            String extractedText = ocrService.extractTextFromImage(file);
            return ResponseEntity.ok(Map.of("text", extractedText));
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body("Failed to process image: " + e.getMessage());
        }
    }
}
