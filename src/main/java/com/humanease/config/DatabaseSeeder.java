package com.humanease.config;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.humanease.entity.Medicine;
import com.humanease.repository.MedicineRepository;
import com.humanease.repository.SavedMedicineRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.io.InputStream;
import java.util.List;

@Component
public class DatabaseSeeder implements CommandLineRunner {

    @Autowired
    private MedicineRepository medicineRepository;

    @Autowired
    private SavedMedicineRepository savedMedicineRepository;

    @Override
    public void run(String... args) throws Exception {
        if (true) {
            System.out.println("Seeding database with 50+ medicines from JSON...");
            // Clear existing partial data to avoid duplicates
            savedMedicineRepository.deleteAll();
            medicineRepository.deleteAll();
            
            ObjectMapper mapper = new ObjectMapper();
            try (InputStream is = getClass().getResourceAsStream("/medicines.json")) {
                if (is != null) {
                    List<Medicine> medicines = mapper.readValue(is, new TypeReference<List<Medicine>>(){});
                    medicineRepository.saveAll(medicines);
                    System.out.println("Default medicines seeded successfully. Total: " + medicines.size());
                } else {
                    System.err.println("Could not find medicines.json in resources!");
                }
            } catch (Exception e) {
                System.err.println("Error seeding database: " + e.getMessage());
            }
        }
    }
}
