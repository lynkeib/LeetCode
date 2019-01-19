#include <iostream>
#include "Node.hpp"
#include "Heap.hpp"

using namespace std;

int main(){
    Node a(0, 8);
    Node b(1, 9);
    Node c(2, 8);
    Node d(3, 7);
    Node e(4, 6);
//    Node *heaptree = new Node[5]{a,b,c,d,e};
//    Heap heap(5, heaptree);
//    cout << heaptree << endl;
//    cout << heap.getheaptree() << endl;

    
    int n = 10;
    int value[10] = {8,14,10,16,7,9,3,2,4,1};
    Node *heaptree = new Node[n];
    for(int i = 0;i < n; i++){
        heaptree[i] = Node(i, value[i]);
    };
    
    Heap heap(n, heaptree);
    heap.show();
    
    cout << "start swap" << endl;
    
    
    
    heap.swap(&heaptree[0], &heaptree[4]);
    
    heap.assignnode();
    
    int uu;
    uu = heap.getheaptree()[5].getleft()->getindex();
    cout << uu << endl;
    heap.show();
        
    return 0;
}
