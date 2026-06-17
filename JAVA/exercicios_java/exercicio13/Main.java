package exercicios_java.exercicio13;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        FiltroGenerico<Produto> filtroProduto = new FiltroGenerico<>();
        List<Produto> estoque = Arrays.asList(
                new Produto("PC Gamer", 15000),
                new Produto("Mouse", 50)
        );

        List<Produto> caros = filtroProduto.filtrar(estoque, p -> p.preco() > 100);
        System.out.println("Produtos caros: " + caros);

        FiltroGenerico<String> filtroString = new FiltroGenerico<>();
        List<String> palavras = Arrays.asList("Java", "Programacao", "POO", "Stream");

        List<String> longas = filtroString.filtrar(palavras, s -> s.length() > 5);
        System.out.println("Palavras longas: " + longas);
    }
}