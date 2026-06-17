package exercicios_java.exercicio2;

public class Livro {
    private String titulo;
    private String autor;
    private boolean disponivel;

    // Construtor
    public Livro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
        this.disponivel = true; // Todo livro começa disponível
    }

    public String getTitulo() { return titulo; }
    public String getAutor() { return autor; }
    public boolean isDisponivel() { return disponivel; }
    public void setDisponivel(boolean disponivel) { this.disponivel = disponivel; }

    @Override
    public String toString() {
        return "Livro: " + titulo + " | Autor: " + autor + " | Disponível: " + (disponivel ? "Sim" : "Não");
    }
}
