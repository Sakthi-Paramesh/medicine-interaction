package com.humanease.repository;

import com.humanease.entity.Medicine;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MedicineRepository extends JpaRepository<Medicine, Long> {
    
    List<Medicine> findByMedicineNameContainingIgnoreCaseOrGenericNameContainingIgnoreCase(String name, String generic);
    
    List<Medicine> findByCategory(String category);
}
