package com.lfernandes.java_spring.aula3.auth.domain.product;

import jakarta.persistence.*;
import lombok.*;

@Table(name = "product")
@Entity(name = "product")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(of = "id")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private String id;
    
    private String name;

    @Column(name = "price_in_cents")
    private Integer price_in_cents;

    public Product(ProductRequestDTO data){
        this.name = data.name();
        this.price_in_cents = data.price_in_cents();
    }
}