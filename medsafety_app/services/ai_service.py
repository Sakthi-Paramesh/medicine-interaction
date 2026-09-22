import google.generativeai as genai
import os

# API key will be retrieved from django settings or env. We'll do it locally here for encapsulation.
from django.conf import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

# Use the recommended fast model
MODEL_NAME = 'gemini-1.5-flash'

def generate_medicine_info(medicine_name):
    prompt = (
        f"You are a medical AI assistant. Provide a highly detailed summary for the medicine '{medicine_name}'. "
        "Return the response in a structured format suitable for parsing, including Generic Name, Category, Uses, Dosage, Side Effects, Food Warnings, Pregnancy Safety, and Interactions."
    )
    
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        ai_response = response.text
        
        # In a real scenario, we'd parse this. For now, mimicking the Java behavior:
        # Returning a dictionary that will be unpacked into a Medicine object
        return {
            "medicine_name": medicine_name,
            "description": "AI Generated Summary:\n" + ai_response,
            "category": "AI Analyzed"
        }
    except Exception as e:
        return {
            "medicine_name": medicine_name,
            "description": f"AI Analysis failed: {str(e)}",
            "category": "Error"
        }

def check_interactions(medicine_names):
    meds = ", ".join(medicine_names)
    prompt = (
        f"You are a clinical pharmacologist. Check for drug interactions between the following medicines: {meds}. "
        "Categorize the interaction as 'Safe', 'Moderate', or 'Dangerous'. Explain why and provide medical warnings."
    )
    
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Analysis failed: {str(e)}"

def answer_follow_up_question(medicine_name, question):
    prompt = (
        f"You are a medical expert. The user is asking about the medicine '{medicine_name}'. "
        f"Question: '{question}'. Provide a safe, clear, and medically accurate response."
    )
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Analysis failed: {str(e)}"

def analyze_prescription(image_file):
    prompt = (
        "You are a medical AI. Carefully read the uploaded prescription image. "
        "1. Extract the names of all the medicines written on it. "
        "2. Briefly explain what each medicine is used for. "
        "3. Most importantly, flag any dangerous interactions between these medicines. "
        "Return the result in clear, formatted HTML (using <ul>, <li>, <strong>, <br> tags). Do not use markdown backticks."
    )
    
    try:
        from PIL import Image
        img = Image.open(image_file)
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content([prompt, img])
        return response.text
    except Exception as e:
        return f"AI Vision Error: {str(e)}"
