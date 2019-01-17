#include <iostream>
#include <typeinfo>

using namespace std;


template<typename T>
void Bubblesort(T *array, int n){
    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < n - i - 1; j++){
            if(array[j] > array[j + 1]){
                T temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}

template<typename T>
void printarray(T array[], int n){
    for(int i = 0; i < n; i++){
        cout<<array[i]<<" ";
    }
    cout << endl;
}

int a[] = {54,6,7,33,2,66,8};
float b[] = {5.4, 6.7, 9.0, 4.0, 14.6, 100.5, 40.7};

int main(){
    int na = sizeof(a) / sizeof(a[0]);
    int nb = sizeof(b) / sizeof(*b);
    Bubblesort(a, na);
    printarray(a, na);
    cout << a << endl;
    cout << typeid(a).name() << endl;
    Bubblesort(b, nb);
    printarray(b, nb);
    cout << b << endl;
    cout << typeid(b).name() << endl;
    return 0;
}

