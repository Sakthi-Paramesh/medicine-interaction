package com.humanease.repository;

import com.humanease.entity.Medicine;
import com.humanease.entity.SavedMedicine;
import com.humanease.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface SavedMedicineRepository extends JpaRepository<SavedMedicine, Long> {
    List<SavedMedicine> findByUserOrderBySavedAtDesc(User user);
    Optional<SavedMedicine> findByUserAndMedicine(User user, Medicine medicine);
    boolean existsByUserAndMedicine(User user, Medicine medicine);
}
