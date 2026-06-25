package com.lfernandes.java_spring.exercicios_spring.exercicio3.service;

import com.lfernandes.java_spring.exercicios_spring.exercicio3.dtos.Veiculo;
import com.lfernandes.java_spring.exercicios_spring.exercicio3.exceptions.VeiculoNaoEncontradoException;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class VeiculoService {
    private final List<Veiculo> frota = new ArrayList<>();

    public VeiculoService() {
        frota.add(new Veiculo("ABC-1234", "Fusca", 1970));
    }

    public Veiculo consultarVeiculo(String placa) {
        return frota.stream()
                .filter(v -> v.placa().equalsIgnoreCase(placa))
                .findFirst()
                .orElseThrow(() -> new VeiculoNaoEncontradoException("Veículo com placa " + placa + " não cadastrado."));
    }
}