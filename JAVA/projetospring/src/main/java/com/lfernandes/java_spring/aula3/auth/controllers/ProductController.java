package com.lfernandes.java_spring.aula3.auth.controllers;

import com.lfernandes.java_spring.aula3.auth.domain.product.Product;
import com.lfernandes.java_spring.aula3.auth.domain.product.ProductRequestDTO;
import com.lfernandes.java_spring.aula3.auth.domain.product.ProductResponseDTO;
import com.lfernandes.java_spring.aula3.auth.repositories.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import jakarta.validation.Valid;

@RestController
@RequestMapping("/product")
public class ProductController {
    @Autowired
    ProductRepository repository;

    @PostMapping
    public ResponseEntity postProduct(@RequestBody @Valid ProductRequestDTO body) {
        System.out.println("Recebido: " + body.name() + " com preço: " + body.price_in_cents());
        Product newProduct = new Product(body);
        this.repository.save(newProduct);
        return ResponseEntity.ok().build();
    }

    @GetMapping
    public ResponseEntity getAllProducts() {
        var productList = this.repository.findAll()
                .stream()
                .map(ProductResponseDTO::new)
                .toList();

        return ResponseEntity.ok(productList);
    }
}
