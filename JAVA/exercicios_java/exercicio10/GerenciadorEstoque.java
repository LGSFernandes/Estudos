package exercicios_java.exercicio10;

import java.util.ArrayList;

public class GerenciadorEstoque {
    private ArrayList<Produto> produtos;

    public GerenciadorEstoque() {
        this.produtos = new ArrayList<>();
    }

    // Busca pelo nome (mais seguro)
    public Produto buscarProduto(String nome) {
        for (Produto p : produtos) {
            if (p.getNome().equalsIgnoreCase(nome)) {
                return p;
            }
        }
        return null; // Retorna null se não achar
    }

    public void adicionarProduto(Produto p) {
        if (p.getPreco() < 0) {
            throw new IllegalArgumentException("Preço não pode ser negativo!");
        }
        produtos.add(p);
    }

    public void venderProduto(String nome, int qtdDesejada) {
        Produto p = buscarProduto(nome);

        if (p == null) {
            System.out.println("Produto não encontrado!");
            return;
        }

        // Validação da regra de negócio
        if (qtdDesejada > p.getQuantidade()) {
            throw new VendaInvalidaException("Estoque insuficiente para: " + nome);
        }

        // Se passar, "vende" (aqui você poderia ter um setQuantidade na classe Produto)
        System.out.println("Venda realizada: " + qtdDesejada + " unidades de " + nome);
    }
}
