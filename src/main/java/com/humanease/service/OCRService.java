package com.humanease.service;

import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

@Service
public class OCRService {

    public String extractTextFromImage(MultipartFile file) throws IOException, TesseractException {
        // Create a temporary file
        Path tempDir = Files.createTempDirectory("");
        File tempFile = tempDir.resolve(file.getOriginalFilename() != null ? file.getOriginalFilename() : "prescription.png").toFile();
        file.transferTo(tempFile);

        Tesseract tesseract = new Tesseract();
        // The path to the tessdata folder (needs to be configured on the server)
        // For development, we set a default path or assume it's in the environment.
        tesseract.setDatapath("C:/Program Files/Tesseract-OCR/tessdata");
        tesseract.setLanguage("eng");
        
        try {
            return tesseract.doOCR(tempFile);
        } finally {
            if (tempFile.exists()) {
                tempFile.delete();
            }
        }
    }
}
