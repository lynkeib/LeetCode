#include <iostream>

using namespace std;

template <class T>
void merge(T arr[], int left, int middle, int right){
    int length_left = middle - left + 1;
    int length_right = right - middle;
    
    T Left[length_left];
    T Right[length_right];
    
    for(int i = 0; i < length_left; i++){
        Left[i] = arr[left + i];
    }
    for(int i = 0; i < length_right; i++){
        Right[i] = arr[middle + 1 + i];
    }
    
    int left_index = 0, right_index = 0, arr_index = 0;
    while((left_index < length_left) & (right_index < length_right)){
        if(Left[left_index] > Right[right_index]){
            arr[arr_index] = Left[left_index];
            left_index ++;
            arr_index ++;
        }
        else{
            arr[arr_index] = Right[right_index];
            right_index ++;
            arr_index ++;
        };
    };
    while(left_index < length_left){
        arr[arr_index] = Left[left_index];
        left_index ++;
        arr_index ++;
    };
    while(right_index < length_right){
        arr[arr_index] = Right[right_index];
        right_index ++;
        arr_index ++;
    };
}

template <class T>
void mergesort(T arr[], int left, int right){
    if (left < right){
        int middle;
        middle = (left + (right - 1)) / 2;
        mergesort(arr, left, middle);
        mergesort(arr, middle + 1, right);
        merge(arr, left, middle, right);
    }
}

template <class T>
void printarr(T arr[], int size){
    for(int i = 0; i < size;i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main() {
    // insert code here...
    int A[] = {1,5,6,3,8,6};
    mergesort(A, 0, 5);
    printarr(A, 6);
}
