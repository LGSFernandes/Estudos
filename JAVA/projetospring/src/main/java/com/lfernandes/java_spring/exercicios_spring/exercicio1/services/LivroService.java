package com.lfernandes.java_spring.exercicios_spring.exercicio1.services;
import com.lfernandes.java_spring.exercicios_spring.exercicio1.models.Livro;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class LivroService {
    private final List<Livro> livros = new ArrayList<>();

    public LivroService() {
        this.livros.add(new Livro("Clean Code", "Robert C. Martin", 2009));
        this.livros.add(new Livro("Design Patterns", "Gang of Four", 1994));
    }

    public void adicionar(Livro l){
        livros.add(l);
    }

    public List<Livro> listarTodos(){
        return livros;
    }
}
