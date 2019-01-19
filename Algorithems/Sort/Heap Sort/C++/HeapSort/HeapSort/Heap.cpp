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

void Heap::assignnode(void){
    for(int i = capacity; i < 0; i--){
        if(i % 2 != 0){
            Node *node;
            Node *signednode;
            node = &heaptree[(i - 1) / 2];
            signednode = &heaptree[i];
            (*node).setleft(signednode);
            
            std::cout << signednode->getindex() << " Assigned to " << node->getindex()<< std::endl;
        }
        else{
            Node *node;
            Node *signednode;
            node = &heaptree[(i - 2) / 2];
            signednode = &heaptree[i];
            node->setright(signednode);
        }
    };
}

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
//
//    }
//}
