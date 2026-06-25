package com.lfernandes.java_spring.aula3.auth.repositories;

import com.lfernandes.java_spring.aula3.auth.domain.product.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, String> {
}
