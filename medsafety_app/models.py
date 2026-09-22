from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = (
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')
    
    # We will let username be the email or username depending on logic, 
    # but Spring Boot code used a generic String for username/email.
    # We use Django's default 'username', 'email', 'password'.
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Medicine(models.fields.Field):
    # Just inheriting from models.Model
    pass

# Redefining properly
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255, null=True, blank=True)
    brand_name = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    uses = models.TextField(null=True, blank=True)
    symptoms = models.TextField(null=True, blank=True)
    dosage = models.TextField(null=True, blank=True)
    side_effects = models.TextField(null=True, blank=True)
    common_side_effects = models.TextField(null=True, blank=True)
    serious_side_effects = models.TextField(null=True, blank=True)
    food_to_eat = models.TextField(null=True, blank=True)
    food_to_avoid = models.TextField(null=True, blank=True)
    alcohol_warning = models.TextField(null=True, blank=True)
    pregnancy_safety = models.TextField(null=True, blank=True)
    breastfeeding_safety = models.TextField(null=True, blank=True)
    kidney_warning = models.TextField(null=True, blank=True)
    liver_warning = models.TextField(null=True, blank=True)
    children_safety = models.TextField(null=True, blank=True)
    elderly_safety = models.TextField(null=True, blank=True)
    driving_warning = models.TextField(null=True, blank=True)
    drug_interactions = models.TextField(null=True, blank=True)
    disease_interactions = models.TextField(null=True, blank=True)
    allergy_warnings = models.TextField(null=True, blank=True)
    storage_instructions = models.TextField(null=True, blank=True)
    missed_dose_instructions = models.TextField(null=True, blank=True)
    overdose_information = models.TextField(null=True, blank=True)
    alternative_medicines = models.TextField(null=True, blank=True)
    similar_medicines = models.TextField(null=True, blank=True)
    prescription_required = models.BooleanField(default=False)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    faqs = models.TextField(null=True, blank=True)
    medical_disclaimer = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.medicine_name


class SavedMedicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_medicines')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='saved_by_users')
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} saved {self.medicine.medicine_name}"


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_history')
    query = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} searched {self.query}"
