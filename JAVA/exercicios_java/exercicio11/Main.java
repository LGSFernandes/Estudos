package exercicios_java.exercicio11;

public class Main {
    public static void main(String[] args){
        Carga c = new Carga("1234", 150, "Pesado");
        Carga c2 = new Carga("5678", 200, "Leve");
        Carga c3 = new Carga("9012", 100, "Médio");

        System.out.println("ID: " + c.id() + ", Preço: " + c.preco() + ", Tipo: " + c.tipo());
        System.out.println("ID: " + c2.id() + ", Preço: " + c2.preco() + ", Tipo: " + c2.tipo());
        System.out.println("ID: " + c3.id() + ", Preço: " + c3.preco() + ", Tipo: " + c3.tipo());

        CentroDistribuicao centro = new CentroDistribuicao();
        centro.adicionarCarga(c);
        centro.adicionarCarga(c2);
        centro.adicionarCarga(c3);

        System.out.println("\nCargas do tipo 'Pesado':");
        centro.listarCargasPorTipo("Pesado").values().forEach(carga -> System.out.println("ID: " + carga.id() + ", Preço: " + carga.preco() + ", Tipo: " + carga.tipo()));
    }
}
