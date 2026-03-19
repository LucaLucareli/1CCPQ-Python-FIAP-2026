import java.util.List;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // =========================================================================
        // 1. O(1) - Complexidade Constante
        // O tempo de execução não depende do tamanho da entrada (n).
        // Não importa se você tem 1 ou 1 milhão de números, o tempo é o mesmo.
        // =========================================================================
        int num1 = 1;
        System.out.println("O(1): Atribuição e acesso direto são instantâneos.");

        // =========================================================================
        // 2. O(n) - Complexidade Linear
        // O tempo cresce na mesma proporção que a lista (n).
        // Se a lista dobra, o tempo de execução dobra.
        // =========================================================================
        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6);
        int soma = 0;
        for (Integer num : nums) { // Percorre a lista exatamente n vezes
            soma += num;
        }
        System.out.println("O(n) - Soma total: " + soma);

        // =========================================================================
        // 3. O(log n) - Complexidade Logarítmica
        // Extremamente eficiente. A cada passo, você descarta METADE dos dados.
        // É o comportamento da Busca Binária em arrays ordenados.
        // =========================================================================
        int[] numsOrdenados = {10, 20, 30, 40, 50, 60, 70, 80};
        int alvo = 70;
        int indice = buscaBinaria(numsOrdenados, alvo);
        System.out.println("O(log n) - Índice do alvo: " + indice);

        // =========================================================================
        // 4. O(n log n) - Complexidade "Linearitmética"
        // É o padrão ouro para ordenação. Quase tão rápido quanto o linear.
        // Ocorre quando dividimos o problema (log n) e processamos cada parte (n).
        // =========================================================================
        int[] numsBaguncados = {6, 1, 3, 2, 5, 4};
        Arrays.sort(numsBaguncados); // Dual-Pivot Quicksort internamente
        System.out.println("O(n log n) - Array ordenado: " + Arrays.toString(numsBaguncados));

        // =========================================================================
        // 5. O(n²) - Complexidade Quadrática
        // Perigoso para grandes volumes de dados.
        // Geralmente causado por loops aninhados (um for dentro de outro for).
        // =========================================================================
        int[] numsPares = {1, 2, 3, 4};
        int somaAlvo = 5;
        System.out.println("O(n²) - Pares que somam " + somaAlvo + ":");
        for (int i = 0; i < numsPares.length; i++) {       // Roda n vezes
            for (int j = 0; j < numsPares.length; j++) {   // Roda n vezes para cada i
                if (numsPares[i] + numsPares[j] == somaAlvo) {
                    System.out.println("  " + numsPares[i] + " + " + numsPares[j]);
                }
            }
        }
    }

    public static int buscaBinaria(int[] array, int alvo) {
        int esquerda = 0;
        int direita = array.length - 1;

        while (esquerda <= direita) {
            int meio = esquerda + ( ( direita - esquerda  ) / 2);

            if (array[meio] == alvo) return meio;

            if (array[meio] < alvo) {
                esquerda = meio + 1;
            } else {
                direita = meio - 1;
            }
        }
        return -1;
    }
}
