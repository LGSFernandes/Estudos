package com.lfernandes.java_spring.exercicios_spring.exercicio2.service;

import com.lfernandes.java_spring.exercicios_spring.exercicio2.configurations.ConfiguracaoFrete;
import org.springframework.stereotype.Service;

@Service
public class FreteService {

    private final ConfiguracaoFrete configuracaoFrete;

    public FreteService(ConfiguracaoFrete configuracaoFrete) {
        this.configuracaoFrete = configuracaoFrete;
    }

    public double calcularFrete(double peso) {
        return (peso * 0.5) + configuracaoFrete.getTaxaFixa();
    }
}