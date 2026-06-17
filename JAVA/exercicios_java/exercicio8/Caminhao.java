package exercicios_java.exercicio8;
import java.util.ArrayList;

public class Caminhao {
    ArrayList<Carga> cargas;
    protected float capacidade;

    public Caminhao(float capacidade){
        this.cargas = new ArrayList<>();
        this.capacidade = capacidade;
    }

    public void adicionarCarga(Carga novaCarga) {
        if (calcularCapacidadeRestante() >= novaCarga.getPeso()) {
            this.cargas.add(novaCarga);
        } else {
            System.out.println("Erro: Carga excede a capacidade do caminhão!");
        }
    }

    public void removerCarga(int id) {
        boolean removido = cargas.removeIf(c -> c.getId() == id);

        if (!removido) {
            System.out.println("Carga com ID " + id + " não encontrada.");
        }
    }

    public double calcularCapacidadeRestante() {
        double pesoTotalAtual = 0;

        for (Carga c : cargas) {
            pesoTotalAtual += c.getPeso();
        }

        return this.capacidade - pesoTotalAtual;
    }

    public ArrayList<Carga> filtrarPorTipo(String tipo) throws TipoNaoEncontradoException {
        ArrayList<Carga> cargasFiltradas = new ArrayList<>();

        // 1. Percorremos a lista original procurando pelo tipo desejado
        for (Carga c : this.cargas) {
            if (c.getTipo().equalsIgnoreCase(tipo)) {
                cargasFiltradas.add(c);
            }
        }

        // 2. Se após o loop a nossa lista estiver vazia, significa que não achamos nada
        if (cargasFiltradas.isEmpty()) {
            throw new TipoNaoEncontradoException("Nenhuma carga do tipo '" + tipo + "' encontrada no caminhão.");
        }

        // 3. Retornamos a lista com os itens encontrados
        return cargasFiltradas;
    }

}
