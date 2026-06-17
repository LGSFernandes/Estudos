package exercicios_java.exercicio12;

public class Main {
    public static void main(String[] args){
        Tarefa tarefa1 = new Tarefa("Comprar leite", 2);
        Tarefa tarefa2 = new Tarefa("Estudar Java", 1);
        Tarefa tarefa3 = new Tarefa("Limpar a casa", 3);
        Tarefa tarefa4 = new Tarefa("Fazer amor", 10);

        GerenciadorTarefas gerenciador = new GerenciadorTarefas();
        gerenciador.adicionarTarefa(tarefa1);
        gerenciador.adicionarTarefa(tarefa2);
        gerenciador.adicionarTarefa(tarefa3);
        gerenciador.adicionarTarefa(tarefa4);

        gerenciador.processarProxima();
        gerenciador.processarProxima();

        System.out.println("Tarefas de alta prioridade:");
        for (Tarefa tarefa : gerenciador.listarTarefasAltaPrioridade()){
            System.out.println(STR."\{tarefa.titulo()} - Prioridade: \{tarefa.prioridade()}");
        }
    }
}
