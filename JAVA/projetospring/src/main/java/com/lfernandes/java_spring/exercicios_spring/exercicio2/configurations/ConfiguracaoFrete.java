package com.lfernandes.java_spring.exercicios_spring.exercicio2.configurations;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class ConfiguracaoFrete {

    @Value("${frete.taxa-fixa}")
    private double taxaFixa;

    public double getTaxaFixa() {
        return taxaFixa;
    }
}
