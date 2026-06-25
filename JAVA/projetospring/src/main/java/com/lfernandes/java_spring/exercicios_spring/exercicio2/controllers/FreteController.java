package com.lfernandes.java_spring.exercicios_spring.exercicio2.controllers;

import com.lfernandes.java_spring.exercicios_spring.exercicio2.service.FreteService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/frete")
public class FreteController {

    private final FreteService freteService;

    public FreteController(FreteService freteService) {
        this.freteService = freteService;
    }

    @GetMapping("/{peso}")
    public double calcularFrete(@PathVariable double peso) {
        return freteService.calcularFrete(peso);
    }
}