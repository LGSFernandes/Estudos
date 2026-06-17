package exercicios_java.exercicio5;
import java.util.ArrayList;

public class Pedido {
    private ArrayList<ItemVenda> itens;

    public Pedido() {
        this.itens = new ArrayList<>();
    }

    public void adicionarItem(ItemVenda item) {
        itens.add(item);
    }

    public double calcularTotal() {
        double total = 0;
        for (ItemVenda i : itens) {
            total += (i.getPrecoUnitario() * i.getQuantidade());
        }
        return total;
    }

    public void aplicarDesconto(double porcentagem) {
        // Regra: apenas se tiver mais de 5 itens no total da lista
        if (itens.size() > 5) {
            double total = calcularTotal();
            double desconto = total * (porcentagem / 100);
            System.out.println("Desconto de " + porcentagem + "% aplicado: -R$" + desconto);
        } else {
            System.out.println("Desconto não aplicado: pedido precisa de mais de 5 itens.");
        }
    }
}
