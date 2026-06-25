package com.lfernandes.java_spring.aula3.auth.repositories;

import com.lfernandes.java_spring.aula3.auth.domain.user.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.security.core.userdetails.UserDetails;

public interface UserRepository extends JpaRepository<User, String> {
    UserDetails findByLogin(String login);
}