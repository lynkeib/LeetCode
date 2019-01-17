#include <iostream>

using namespace std;




class man{
private:
    int a;
public:
    int b;
};

class Node{
private:
    Node left_child();
    Node right_child();
    Node parent();
    int index;
    int value;
    
public:
    Node(int index, int value): index(0), value(0), left_child(NULL), right(NULL), parent(NULL){
        index = index;
        value = value;
    };
    ~Node();
    Node getleft(){
        return left_child;
    };
    
};
