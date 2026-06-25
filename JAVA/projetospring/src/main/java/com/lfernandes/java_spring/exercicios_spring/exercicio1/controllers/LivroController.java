package com.lfernandes.java_spring.exercicios_spring.exercicio1.controllers;
import com.lfernandes.java_spring.exercicios_spring.exercicio1.models.Livro;
import com.lfernandes.java_spring.exercicios_spring.exercicio1.services.LivroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/livros")
public class LivroController {

    @Autowired
    private LivroService livros;

    @GetMapping
    public String listarLivros(){
        if (livros.listarTodos().isEmpty()) {
            return "Nenhum livro cadastrado.";
        } else {
            StringBuilder sb = new StringBuilder();
            for (Livro l : livros.listarTodos()) {
                sb.append("Título: ").append(l.titulo()).append(" | Autor: ").append(l.autor()).append(" | Ano: ").append(l.ano()).append("\n");
            }
            return sb.toString();
        }
    }

    @PostMapping
    public String adicionar(@RequestBody Livro livro) {
        livros.adicionar(livro);
        return "Livro: '" + livro.titulo() + "' adicionado com sucesso.";
    }
}
