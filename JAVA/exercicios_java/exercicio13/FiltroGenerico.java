package exercicios_java.exercicio13;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class FiltroGenerico<T> {

    public List<T> filtrar(List<T> lista, Predicate<T> condicao) {
        List<T> resultado = new ArrayList<>();

        for (T item : lista) {
            if (condicao.test(item)) {
                resultado.add(item);
            }
        }
        return resultado;
    }
}