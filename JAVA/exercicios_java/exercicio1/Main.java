package exercicios_java.exercicio1;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        ArrayList<Double> lista = new ArrayList<>();

        while(true) {
            System.out.print("Digite o gasto (-1 para parar): R$ ");
            double valor = sc.nextDouble();

            if (valor == -1){
                break;
            }

            lista.add(valor);
        }

        if (lista.isEmpty()) {
            System.out.println("Nenhum Gasto foi Registrado.");
        } else {
            double gastoTotal = 0.0;
            double maior = lista.getFirst();
            double menor = lista.getFirst();

            for (double num : lista) {
                gastoTotal += num;
                if (num > maior) maior = num;
                if (num < menor) menor = num;
            }

            double media = gastoTotal / lista.size();

            System.out.println(STR."Gasto Total: R$\{String.format("%.2f", gastoTotal)}");
            System.out.println(STR."Média de Gasto: R$\{String.format("%.2f", media)}");
            System.out.println(STR."Maior Gasto: R$\{String.format("%.2f", maior)}");
            System.out.println(STR."Menor Gasto: R$\{String.format("%.2f", menor)}");
        }

        sc.close();
    }
}