// ========================================================================================================================
// Beecrowd - 1162 - Organizador de Vagoes - Nivel 5
// ========================================================================================================================
// Teoria: Dividir e Conquistar
// Algoritmo utilizado: Algoritmo de contagem de inversoes
// ========================================================================================================================
#include <iostream>
#include <vector>
using namespace std;

// calcula a quantidade de inversoes recursivamente
int contarInversoes(vector<int>& vetor, int ind_esq, int ind_dir) {
    if (ind_dir <= ind_esq) {
        return 0;
    }
    int ind_meio = (ind_esq + ind_dir) / 2;
    int qtd_inversoes = contarInversoes(vetor, ind_esq, ind_meio) +
                        contarInversoes(vetor, ind_meio + 1, ind_dir);
    int i = ind_esq;
    int j = ind_meio + 1;
    int inv = 0;
    vector<int> vetor_aux;
    while (i <= ind_meio && j <= ind_dir) {
        if (vetor[i] <= vetor[j]) {
            vetor_aux.push_back(vetor[i]);
            i++;
        } else {
            inv += ind_meio - i + 1;
            vetor_aux.push_back(vetor[j]);
            j++;
        }
    }
    while (i <= ind_meio) {
        vetor_aux.push_back(vetor[i]);
        i++;
    }
    while (j <= ind_dir) {
        vetor_aux.push_back(vetor[j]);
        j++;
    }
    for (int k = ind_esq; k <= ind_dir; k++) {
        vetor[k] = vetor_aux[k - ind_esq];
    }
    return qtd_inversoes + inv;
}

int main() {
    int casos_teste;
    cin >> casos_teste;
    for (int t = 0; t < casos_teste; t++) {
        int tamanho_trem;
        cin >> tamanho_trem;
        vector<int> vagoes(tamanho_trem);
        for (int i = 0; i < tamanho_trem; i++) {
            cin >> vagoes[i];
        }
        int qtd_inversoes = contarInversoes(vagoes, 0, vagoes.size() - 1);
        cout << "Optimal train swapping takes " << qtd_inversoes << " swaps." << endl;
    }
    return 0;
}
