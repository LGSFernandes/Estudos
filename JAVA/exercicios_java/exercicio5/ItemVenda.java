package exercicios_java.exercicio5;

public class ItemVenda {
    private String nome;
    private double precoUnitario;
    private int quantidade;

    public ItemVenda(String nome, double precoUnitario, int quantidade) {
        this.nome = nome;
        this.precoUnitario = precoUnitario;
        this.quantidade = quantidade;
    }

    // Getters
    public double getPrecoUnitario() { return precoUnitario; }
    public int getQuantidade() { return quantidade; }
    public String getNome() { return nome; }
}