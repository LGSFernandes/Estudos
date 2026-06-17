package exercicios_java.exercicio2;

public class Main {
    static void main(String[] args) {
        Biblioteca bib = new Biblioteca();

        bib.adicionarLivro(new Livro("Dom Casmurro", "Machado de Assis"));
        bib.adicionarLivro(new Livro("O Hobbit", "J.R.R. Tolkien"));

        bib.listarLivros();

        // Testando empréstimos
        bib.emprestarLivro("O Hobbit");
        bib.emprestarLivro("O Hobbit");
        bib.emprestarLivro("Harry Potter");

        bib.listarLivros();
    }
}