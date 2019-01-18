//
//  Node.cpp
//  HeapSort
//
//  Created by Chengyin Liu on 1/17/19.
//  Copyright © 2019 Chengyin Liu. All rights reserved.
//

#include "Node.hpp"

Node::Node(int index, int value):index(NULL), value(NULL){
    this->index = index;
    this->value = value;
    left_child = NULL;
    right_child = NULL;
    parent = NULL;
};

Node::Node(){
    index = NULL;
    value = NULL;
    left_child = NULL;
    right_child = NULL;
    parent = NULL;
};

Node::~Node(){};

void Node::setleft(Node *node){
    this->left_child = node;
};

void Node::setright(Node *node){
    this->right_child = node;
};

void Node::setparent(Node *node){
    this->parent = node;
};
