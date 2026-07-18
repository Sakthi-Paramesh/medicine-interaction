package com.humanease.entity;

import jakarta.persistence.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;

@Entity
@Table(name = "medicines")
public class Medicine {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String medicineName;

    private String genericName;
    private String brandName;
    private String imageUrl;
    private String category;

    @Column(columnDefinition = "TEXT")
    private String uses;

    @Column(columnDefinition = "TEXT")
    private String symptoms;

    @Column(columnDefinition = "TEXT")
    private String dosage;

    @Column(columnDefinition = "TEXT")
    private String sideEffects;

    @Column(columnDefinition = "TEXT")
    private String commonSideEffects;

    @Column(columnDefinition = "TEXT")
    private String seriousSideEffects;

    // Diet & Lifestyle Warnings
    @Column(columnDefinition = "TEXT")
    private String foodToEat;

    @Column(columnDefinition = "TEXT")
    private String foodToAvoid;

    @Column(columnDefinition = "TEXT")
    private String alcoholWarning;

    // Patient Safety Warnings
    @Column(columnDefinition = "TEXT")
    private String pregnancySafety;

    @Column(columnDefinition = "TEXT")
    private String breastfeedingSafety;

    @Column(columnDefinition = "TEXT")
    private String kidneyWarning;

    @Column(columnDefinition = "TEXT")
    private String liverWarning;

    @Column(columnDefinition = "TEXT")
    private String childrenSafety;

    @Column(columnDefinition = "TEXT")
    private String elderlySafety;

    @Column(columnDefinition = "TEXT")
    private String drivingWarning;

    // Interactions
    @Column(columnDefinition = "TEXT")
    private String drugInteractions;

    @Column(columnDefinition = "TEXT")
    private String diseaseInteractions;

    @Column(columnDefinition = "TEXT")
    private String allergyWarnings;

    // Instructions
    @Column(columnDefinition = "TEXT")
    private String storageInstructions;

    @Column(columnDefinition = "TEXT")
    private String missedDoseInstructions;

    @Column(columnDefinition = "TEXT")
    private String overdoseInformation;

    // Related
    @Column(columnDefinition = "TEXT")
    private String alternativeMedicines;

    @Column(columnDefinition = "TEXT")
    private String similarMedicines;

    private boolean prescriptionRequired;
    private String manufacturer;

    @Column(columnDefinition = "TEXT")
    private String description;

    @Column(columnDefinition = "TEXT")
    private String faqs;

    @Column(columnDefinition = "TEXT")
    private String medicalDisclaimer;

    @CreationTimestamp
    @Column(updatable = false)
    private LocalDateTime createdAt;

    @UpdateTimestamp
    private LocalDateTime updatedAt;

    public Medicine() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getMedicineName() { return medicineName; }
    public void setMedicineName(String medicineName) { this.medicineName = medicineName; }

    public String getGenericName() { return genericName; }
    public void setGenericName(String genericName) { this.genericName = genericName; }

    public String getBrandName() { return brandName; }
    public void setBrandName(String brandName) { this.brandName = brandName; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getUses() { return uses; }
    public void setUses(String uses) { this.uses = uses; }

    public String getSymptoms() { return symptoms; }
    public void setSymptoms(String symptoms) { this.symptoms = symptoms; }

    public String getDosage() { return dosage; }
    public void setDosage(String dosage) { this.dosage = dosage; }

    public String getSideEffects() { return sideEffects; }
    public void setSideEffects(String sideEffects) { this.sideEffects = sideEffects; }

    public String getCommonSideEffects() { return commonSideEffects; }
    public void setCommonSideEffects(String commonSideEffects) { this.commonSideEffects = commonSideEffects; }

    public String getSeriousSideEffects() { return seriousSideEffects; }
    public void setSeriousSideEffects(String seriousSideEffects) { this.seriousSideEffects = seriousSideEffects; }

    public String getFoodToEat() { return foodToEat; }
    public void setFoodToEat(String foodToEat) { this.foodToEat = foodToEat; }

    public String getFoodToAvoid() { return foodToAvoid; }
    public void setFoodToAvoid(String foodToAvoid) { this.foodToAvoid = foodToAvoid; }

    public String getAlcoholWarning() { return alcoholWarning; }
    public void setAlcoholWarning(String alcoholWarning) { this.alcoholWarning = alcoholWarning; }

    public String getPregnancySafety() { return pregnancySafety; }
    public void setPregnancySafety(String pregnancySafety) { this.pregnancySafety = pregnancySafety; }

    public String getBreastfeedingSafety() { return breastfeedingSafety; }
    public void setBreastfeedingSafety(String breastfeedingSafety) { this.breastfeedingSafety = breastfeedingSafety; }

    public String getKidneyWarning() { return kidneyWarning; }
    public void setKidneyWarning(String kidneyWarning) { this.kidneyWarning = kidneyWarning; }

    public String getLiverWarning() { return liverWarning; }
    public void setLiverWarning(String liverWarning) { this.liverWarning = liverWarning; }

    public String getChildrenSafety() { return childrenSafety; }
    public void setChildrenSafety(String childrenSafety) { this.childrenSafety = childrenSafety; }

    public String getElderlySafety() { return elderlySafety; }
    public void setElderlySafety(String elderlySafety) { this.elderlySafety = elderlySafety; }

    public String getDrivingWarning() { return drivingWarning; }
    public void setDrivingWarning(String drivingWarning) { this.drivingWarning = drivingWarning; }

    public String getDrugInteractions() { return drugInteractions; }
    public void setDrugInteractions(String drugInteractions) { this.drugInteractions = drugInteractions; }

    public String getDiseaseInteractions() { return diseaseInteractions; }
    public void setDiseaseInteractions(String diseaseInteractions) { this.diseaseInteractions = diseaseInteractions; }

    public String getAllergyWarnings() { return allergyWarnings; }
    public void setAllergyWarnings(String allergyWarnings) { this.allergyWarnings = allergyWarnings; }

    public String getStorageInstructions() { return storageInstructions; }
    public void setStorageInstructions(String storageInstructions) { this.storageInstructions = storageInstructions; }

    public String getMissedDoseInstructions() { return missedDoseInstructions; }
    public void setMissedDoseInstructions(String missedDoseInstructions) { this.missedDoseInstructions = missedDoseInstructions; }

    public String getOverdoseInformation() { return overdoseInformation; }
    public void setOverdoseInformation(String overdoseInformation) { this.overdoseInformation = overdoseInformation; }

    public String getAlternativeMedicines() { return alternativeMedicines; }
    public void setAlternativeMedicines(String alternativeMedicines) { this.alternativeMedicines = alternativeMedicines; }

    public String getSimilarMedicines() { return similarMedicines; }
    public void setSimilarMedicines(String similarMedicines) { this.similarMedicines = similarMedicines; }

    public boolean isPrescriptionRequired() { return prescriptionRequired; }
    public void setPrescriptionRequired(boolean prescriptionRequired) { this.prescriptionRequired = prescriptionRequired; }

    public String getManufacturer() { return manufacturer; }
    public void setManufacturer(String manufacturer) { this.manufacturer = manufacturer; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public String getFaqs() { return faqs; }
    public void setFaqs(String faqs) { this.faqs = faqs; }

    public String getMedicalDisclaimer() { return medicalDisclaimer; }
    public void setMedicalDisclaimer(String medicalDisclaimer) { this.medicalDisclaimer = medicalDisclaimer; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }

    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
}
