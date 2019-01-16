#include <iostream>

using namespace std;

void swap(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

void Bubblesort(int array[], int n){
    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < n - i - 1; j++){
            if(array[j] > array[j + 1]){
                swap(&array[j], &array[j+1]);
            }
        }
    }
}

void printarray(int array[], int n){
    for(int i = 0; i < n; i++){
        cout<<array[i]<<" ";
    }
    cout << endl;
}

int a[] = {54,6,7,33,2,66,8};

int main(){
    int n = sizeof(a) / sizeof(a[0]);
    Bubblesort(a, n);
    printarray(a, n);
    return 0;
}

