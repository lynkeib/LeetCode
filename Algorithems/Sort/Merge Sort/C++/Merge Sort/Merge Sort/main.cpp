#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

template <class T>
void mergesort(vector <T> arr){
    if(arr.size() > 1)
    {
        int middle;
        middle = arr.size() / 2;
        vector <T> left(middle);
        for(int i = 0; i < middle; i++){left.push_back(arr[i]);}
        vector <T> right(arr.size() - middle);
        for(int i = middle; i < arr.size(); i++){right.push_back(arr[i]);}
        mergesort(left);
        mergesort(right);
        int left_index = 0;
        int right_index = 0;
        int arr_index = 0;
        while((left_index < arr.size()) & (right_index < arr.size()))
        {
            if(left[left_index] > right[right_index])
            {
                arr[arr_index] = left[left_index];
                left_index += 1;
                arr_index += 1;
            }
            else
            {
                arr[arr_index] = right[right_index];
                right_index += 1;
                arr_index += 1;
            };
        while(left_index < arr.size())
            {
            arr[arr_index] = left[left_index];
            arr_index += 1;
            left_index += 1;
            };
        while(right_index < arr.size())
            {
            arr[arr_index] = right[right_index];
            arr_index += 1;
            right_index += 1;
            };
        };
    };
}

template <class T>
void printarr(vector <T> arr){
    for(int i = 0; i < arr.size();i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main()
{
    // insert code here...
    vector <int> a;
    a = {1,5,6,3,8,6};
    mergesort(a);
    printarr(a);
    vector <int> b;
    b ={1,2,3,4,5};
    cout << b.size() / 2<< endl;
    vector <int> c;
    c = {1,2,3,4,5};
    vector <int> d;
    for(int i = 0; i < 4; i++) {d.push_back(c[i]);}
    printarr(d);
    return 0;
}
