package exercicios_java.exercicio12;
import java.util.stream.Collectors;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class GerenciadorTarefas {
    private Queue<Tarefa> tarefas;

    public GerenciadorTarefas() {
        this.tarefas = new LinkedList<>();
    }

    public void adicionarTarefa(Tarefa f){
        tarefas.add(f);
    }

    public String processarProxima(){
        if (tarefas.isEmpty()){
            return (STR."Fila está vazia. Nenhuma tarefa para processar.");
        }

        Tarefa tarefa = tarefas.poll();
        System.out.println(STR."Próxima Tarefa: \{tarefa.titulo()}");

        return "";
    }

    public List<Tarefa> listarTarefasAltaPrioridade() {
        return tarefas
                .stream()
                .filter(t -> t.prioridade() > 5)
                .collect(Collectors.toList());
    }
}
