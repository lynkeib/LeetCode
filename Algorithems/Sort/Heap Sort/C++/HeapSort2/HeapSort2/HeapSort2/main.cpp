#include <iostream>

using namespace std;

void show(int *list, int lenght){
    for (int i = 0; i < lenght; ++i){
        cout << list[i] << " ";
    }
    cout << "\n";
}

void Heapify(int *list, int length, int heapnode){
    int largest = heapnode;
    int left = 2 * heapnode + 1;
    int right = 2 * heapnode + 2;
    if (left < length && list[left] > list[largest])
        largest = left;
    if (right < length && list[right] > list[largest])
        largest = right;
    if (largest != heapnode){
        swap(list[heapnode], list[largest]);
        Heapify(list, length, largest);
    }
}

void HeapSort(int *list, int n){
    for (int i = n / 2 - 1; i >= 0; i--)
        Heapify(list, n, i);
    for (int i = n - 1; i >= 0; i--){
        swap(list[0], list[i]);
        Heapify(list, i, 0);
    }
}

int main(){
    int list[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(list)/sizeof(*list);
    HeapSort(list, n);
    show(list, n);
}
