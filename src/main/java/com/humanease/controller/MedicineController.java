package com.humanease.controller;

import com.humanease.entity.Medicine;
import com.humanease.service.MedicineService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/medicines")
public class MedicineController {

    @Autowired
    private MedicineService medicineService;

    @Autowired
    private com.humanease.service.AIAssistantService aiAssistantService;

    @GetMapping("/search")
    public ResponseEntity<List<Medicine>> search(@RequestParam String q) {
        return ResponseEntity.ok(medicineService.searchMedicines(q));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Medicine> getMedicine(@PathVariable Long id) {
        return medicineService.getMedicineById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Medicine> addMedicine(@RequestBody Medicine medicine) {
        return ResponseEntity.ok(medicineService.saveMedicine(medicine));
    }

    @PostMapping("/scan")
    public ResponseEntity<String> scanPrescription(@RequestParam("image") org.springframework.web.multipart.MultipartFile image) {
        try {
            return ResponseEntity.ok(aiAssistantService.analyzePrescription(image));
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Error analyzing image: " + e.getMessage());
        }
    }
}
