//
//  Node.hpp
//  HeapSort
//
//  Created by Chengyin Liu on 1/17/19.
//  Copyright © 2019 Chengyin Liu. All rights reserved.
//

#ifndef Node_hpp
#define Node_hpp

#include <stdio.h>

class Node{
private:
    Node *left_child;
    Node *right_child;
    Node *parent;
    int index;
    int value;
public:
    //Constructor
    Node(int index, int value);
    Node();
    //Destructor
    ~Node();
    Node *getleft(void){return left_child;}
    Node *getright(void){return right_child;}
    Node *getparent(void){return parent;}
    int getindex(void){return index;}
    int getvalue(void){return value;}
    void setleft(Node *node);
    void setright(Node *node);
    void setparent(Node *node);
};

#endif /* Node_hpp */
