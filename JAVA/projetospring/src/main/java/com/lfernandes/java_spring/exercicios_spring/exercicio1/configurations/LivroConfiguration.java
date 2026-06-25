package com.lfernandes.java_spring.exercicios_spring.exercicio1.configurations;

import com.lfernandes.java_spring.exercicios_spring.exercicio1.models.Livro;
import com.lfernandes.java_spring.exercicios_spring.exercicio1.services.LivroService;
import org.springframework.context.annotation.Configuration;

@Configuration
public class LivroConfiguration {
    public LivroService livroService() {
        LivroService service = new LivroService();
        service.adicionar(new Livro("Clean Code", "Robert C. Martin", 2009));
        service.adicionar(new Livro("Design Patterns", "Gang of Four", 1994));
        return service;
    }
}
