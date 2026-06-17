package exercicios_java.exercicio10;

public class Produto {
    protected String nome;
    protected double preco;
    private int quantidade;

    public Produto(String nome, double preco, int quantidade){
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    public String getNome() {
        return nome;
    }

    public void setQuantidade(int novaQtd) {
        this.quantidade = novaQtd;
    }


    public double getPreco() {
        return preco;
    }

    public int getQuantidade() {
        return quantidade;
    }
}
