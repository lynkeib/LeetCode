//
//  Heap.hpp
//  HeapSort
//
//  Created by Chengyin Liu on 1/17/19.
//  Copyright © 2019 Chengyin Liu. All rights reserved.
//

#ifndef Heap_hpp
#define Heap_hpp

#include <stdio.h>
#include "Node.hpp"

class Heap{
private:
    Node *heaptree;
    int capacity;
//    void maxheapify(int index);
public:
    Heap(int cap, Node *heaplist);
    ~Heap();
    void assignnode(void);
    Node *getheaptree(){return heaptree;}
    void swap(Node *a, Node *b);
    void show();
};

#endif /* Heap_hpp */
