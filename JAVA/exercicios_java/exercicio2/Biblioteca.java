package exercicios_java.exercicio2;
import java.util.ArrayList;

public class Biblioteca {
    private ArrayList<Livro> livros;

    public Biblioteca() {
        this.livros = new ArrayList<>();
    }

    public void adicionarLivro(Livro l) {
        livros.add(l);
    }

    public void emprestarLivro(String titulo) {
        boolean encontrado = false;

        for (Livro l : livros) {
            if (l.getTitulo().equalsIgnoreCase(titulo)) {
                encontrado = true;
                if (l.isDisponivel()) {
                    l.setDisponivel(false);
                    System.out.println("Sucesso: O livro '" + titulo + "' foi emprestado.");
                } else {
                    System.out.println("Erro: O livro '" + titulo + "' já está emprestado.");
                }
                break;
            }
        }

        if (!encontrado) {
            System.out.println("Erro: Livro '" + titulo + "' não encontrado na lista de Livros.");
        }
    }

    public void listarLivros() {
        System.out.println("\n--- Livros da Biblioteca ---");
        for (Livro l : livros) {
            System.out.println(l);
        }
    }
}
