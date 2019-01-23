#include <iostream>
#include <vector>

using namespace std;

template <class T>
vector <T> insertionsort(vector <T> lst){
    vector <T> temp_list(lst);
    for(int i = 1; i < temp_list.size();i++){
        T key = temp_list[i];
        int j = i - 1;
        while((j > 0) & (temp_list[j] > key)){
            temp_list[j + 1] = temp_list[j];
            j -= 1;
        }
        temp_list[j+1] = key;
    }
    return temp_list;
};

template <class T>
void printvector(vector <T> lst){
    for(int i = 0; i < lst.size();i++){
        cout << lst[i] << " ";
    }
    cout << endl;
};

int main() {
    vector <int> a;
    a = {-5,-8,4,6,3,3,6,8};
    vector <int> lis1;
    lis1 = insertionsort(a);
    printvector(lis1);
    
    vector <float> b;
    b = {-6.3,-8,5,6,3,10.9,6,2.8};
    vector <float> lis2;
    lis2 = insertionsort(b);
    printvector(lis2);
    return 0;
}
