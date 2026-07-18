package com.humanease.controller;

import com.humanease.entity.Medicine;
import com.humanease.service.AIAssistantService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.Map;

@Controller
public class AIController {

    @Autowired
    private AIAssistantService aiAssistantService;

    @GetMapping("/medicine/ai")
    public String analyzeUnknownMedicine(@RequestParam String q, Model model) {
        Medicine med = aiAssistantService.generateMedicineInfo(q);
        // We render this dynamically to the medicine_detail template but flag it as AI
        model.addAttribute("medicine", med);
        model.addAttribute("isAiGenerated", true);
        model.addAttribute("query", q);
        return "medicine_ai_detail";
    }

    @GetMapping("/interaction")
    public String interactionPage() {
        return "interaction";
    }

    @GetMapping("/api/ai/interaction")
    @ResponseBody
    public Map<String, String> checkInteraction(@RequestParam String meds) {
        String[] medicineNames = meds.split(",");
        String response = aiAssistantService.checkInteractions(medicineNames);
        return Map.of("analysis", response);
    }
}
