package exercicios_java.exercicio5;

public class Main {
    public static void main(String[] args) {
        Pedido meuPedido = new Pedido();

        // Adicionando alguns itens
        meuPedido.adicionarItem(new ItemVenda("Café", 10.0, 2));
        meuPedido.adicionarItem(new ItemVenda("Pão", 5.0, 10));

        System.out.println("Total do pedido: R$" + meuPedido.calcularTotal());

        // Tentando aplicar desconto (não deve funcionar pois só temos 2 itens na lista)
        meuPedido.aplicarDesconto(10.0);
    }
}