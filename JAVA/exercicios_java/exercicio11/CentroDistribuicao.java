package exercicios_java.exercicio11;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CentroDistribuicao {
    Map<String, Carga> cargas = new HashMap<>();

    public void adicionarCarga(Carga c){
        cargas.put(c.id(), c);
    }

    public Carga buscarCarga(String id){
        return cargas.get(id);
    }

    public Map<String, Carga> listarCargasPorTipo(String tipo){
        List<String> carga = cargas.values().stream()
                .filter(c -> c.tipo().equals(tipo))
                .map(Carga::id)
                .collect(Collectors.toList());

        return cargas.entrySet().stream()
                .filter(e -> carga.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }
}
