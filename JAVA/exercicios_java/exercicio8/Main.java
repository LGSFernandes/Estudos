package exercicios_java.exercicio8;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Caminhao caminhao = new Caminhao(1000.0f);

        caminhao.adicionarCarga(new Carga(1, 200.0, "Frágil"));
        caminhao.adicionarCarga(new Carga(2, 300.0, "Normal"));

        try {
            ArrayList<Carga> frageis = caminhao.filtrarPorTipo("Frágil");

            for (Carga c : frageis) {
                System.out.println("Carga encontrada: ID " + c.getId());
            }
        } catch (TipoNaoEncontradoException e) {
            System.out.println("Aviso: " + e.getMessage());
        }
    }
}