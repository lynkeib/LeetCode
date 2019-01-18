//
//  Heap.cpp
//  HeapSort
//
//  Created by Chengyin Liu on 1/17/19.
//  Copyright © 2019 Chengyin Liu. All rights reserved.
//

#include "Heap.hpp"
#include <iostream>

Heap::Heap(int cap, Node *heaplist){
    capacity = cap;
    heaptree = heaplist;
};

Heap::~Heap(){};

void Heap::swap(Node *a, Node *b){
    Node temp = *a;
    *a = *b;
    *b = temp;
};

void Heap::show(){
    for(int i = 0;i<capacity;i++){
        std::cout << "Node Number " << i << " " << heaptree[i].getvalue() << std::endl;
    };
};

//void Heap::maxheapify(int index){
//    if(heaptree[index]){
//
//    }
//}
