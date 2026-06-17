package exercicios_java.exercicio10;
import java.awt.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        GerenciadorEstoque estoque = new GerenciadorEstoque();

        estoque.adicionarProduto(new Produto("PC Gamer", 15000, 50));
        estoque.adicionarProduto(new Produto("Smartphone", 8000, 200));

        try {
            estoque.venderProduto("PC Gamer", 10);
        } catch (VendaInvalidaException e) {
            System.out.println(e.getMessage());
        }

    }
}
