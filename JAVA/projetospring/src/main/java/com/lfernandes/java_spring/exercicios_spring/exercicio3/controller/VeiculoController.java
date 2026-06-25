package com.lfernandes.java_spring.exercicios_spring.exercicio3.controller;

import com.lfernandes.java_spring.exercicios_spring.exercicio3.dtos.Veiculo;
import com.lfernandes.java_spring.exercicios_spring.exercicio3.service.VeiculoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/veiculos")
public class VeiculoController {

    private final VeiculoService service;

    public VeiculoController(VeiculoService service) {
        this.service = service;
    }

    @GetMapping("/{placa}")
    public Veiculo buscar(@PathVariable String placa) {
        return service.consultarVeiculo(placa);
    }
}
