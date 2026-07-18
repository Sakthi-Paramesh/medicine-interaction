package com.humanease.controller;

import com.humanease.entity.Medicine;
import com.humanease.entity.SavedMedicine;
import com.humanease.entity.SearchHistory;
import com.humanease.entity.User;
import com.humanease.repository.MedicineRepository;
import com.humanease.repository.SavedMedicineRepository;
import com.humanease.repository.SearchHistoryRepository;
import com.humanease.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/user")
public class UserInteractionController {

    @Autowired
    private SavedMedicineRepository savedMedicineRepository;

    @Autowired
    private SearchHistoryRepository searchHistoryRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private MedicineRepository medicineRepository;

    private User getCurrentUser() {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || !auth.isAuthenticated() || auth.getPrincipal().equals("anonymousUser")) {
            return null;
        }
        return userRepository.findByUsername(auth.getName()).orElse(null);
    }

    @PostMapping("/save/{medicineId}")
    public ResponseEntity<?> saveMedicine(@PathVariable Long medicineId) {
        User user = getCurrentUser();
        if (user == null) return ResponseEntity.status(401).body("Unauthorized");

        Optional<Medicine> med = medicineRepository.findById(medicineId);
        if (med.isEmpty()) return ResponseEntity.notFound().build();

        if (savedMedicineRepository.existsByUserAndMedicine(user, med.get())) {
            return ResponseEntity.ok(Map.of("message", "Already saved", "saved", true));
        }

        SavedMedicine saved = new SavedMedicine();
        saved.setUser(user);
        saved.setMedicine(med.get());
        savedMedicineRepository.save(saved);

        return ResponseEntity.ok(Map.of("message", "Medicine saved successfully", "saved", true));
    }

    @DeleteMapping("/save/{medicineId}")
    public ResponseEntity<?> unsaveMedicine(@PathVariable Long medicineId) {
        User user = getCurrentUser();
        if (user == null) return ResponseEntity.status(401).body("Unauthorized");

        Optional<Medicine> med = medicineRepository.findById(medicineId);
        if (med.isEmpty()) return ResponseEntity.notFound().build();

        Optional<SavedMedicine> saved = savedMedicineRepository.findByUserAndMedicine(user, med.get());
        if (saved.isPresent()) {
            savedMedicineRepository.delete(saved.get());
            return ResponseEntity.ok(Map.of("message", "Medicine removed from saved list", "saved", false));
        }
        return ResponseEntity.ok(Map.of("message", "Not saved previously", "saved", false));
    }

    @GetMapping("/save/status/{medicineId}")
    public ResponseEntity<?> checkSaveStatus(@PathVariable Long medicineId) {
        User user = getCurrentUser();
        if (user == null) return ResponseEntity.ok(Map.of("saved", false));

        Optional<Medicine> med = medicineRepository.findById(medicineId);
        if (med.isEmpty()) return ResponseEntity.ok(Map.of("saved", false));

        boolean exists = savedMedicineRepository.existsByUserAndMedicine(user, med.get());
        return ResponseEntity.ok(Map.of("saved", exists));
    }

    @GetMapping("/recent-searches")
    public ResponseEntity<List<String>> getRecentSearches() {
        User user = getCurrentUser();
        if (user == null) return ResponseEntity.ok(List.of());

        List<SearchHistory> history = searchHistoryRepository.findTop10ByUserOrderBySearchedAtDesc(user);
        List<String> queries = history.stream().map(SearchHistory::getQuery).distinct().collect(Collectors.toList());
        return ResponseEntity.ok(queries);
    }

    @GetMapping("/saved")
    public ResponseEntity<List<Medicine>> getSavedMedicines() {
        User user = getCurrentUser();
        if (user == null) return ResponseEntity.ok(List.of());

        List<SavedMedicine> saved = savedMedicineRepository.findByUserOrderBySavedAtDesc(user);
        List<Medicine> medicines = saved.stream().map(SavedMedicine::getMedicine).collect(Collectors.toList());
        return ResponseEntity.ok(medicines);
    }

    @PostMapping("/search-history")
    public ResponseEntity<?> logSearchHistory(@RequestParam String query) {
        User user = getCurrentUser();
        if (user != null && query != null && query.trim().length() > 0) {
            SearchHistory history = new SearchHistory();
            history.setUser(user);
            history.setQuery(query.trim());
            searchHistoryRepository.save(history);
        }
        return ResponseEntity.ok().build();
    }
}
