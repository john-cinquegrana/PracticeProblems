
/*
 * File: flatten.cpp
 * File Created:  Tuesday, 2nd March 2021
 * Author: John Cinquegrana, Nikolas Stefanov, Liam Nagel (jcinqueg@stevens.edu, nstefano@stevens.edu, lnagel@stevens.edu)
 * Stevens 2021s
 * Pledge: I pledge my honor I have abided by the Stevens Honor system.
 * Description: TODO Auto-Generated Description.
 */


#include <cstddef>
#include <stack>

// Definition for a Node.
// class Node {
// public:
//     int val;
//     Node* prev;
//     Node* next;
//     Node* child;
// };

class Solution {
    public:
        Node* flatten(Node* head) {
            if( head == nullptr ) return head;
            Node* current = head;
            std::stack<Node*> st;
            bool flag = false;
            while(!flag){
                //Go through List
                while( current->next != nullptr || current->child != nullptr ) {
                    //While we have a Next element
                    if( current->child != nullptr ){
                        //If there is a child, push next element onto stack and set current's next
                        //  to child and child's prev to current
                        if( current->next != nullptr ) st.push(current->next);
                        current->next = current->child;
                        current->child = nullptr;
                        current->next->prev = current;
                    }
                    //  If there was no child, go on as normal
                    //  If there was a child, it would now be set as next
                    current = current->next;
                      
                }
                if(st.empty()){
                    //If we do not have a next element and the stack is empty, then we are done
                    flag = true;
                    break;
                }
                else{
                    //Otherwise we must pop the stack and iterate through what was on the stack until we run through again
                    current->next = st.top();
                    st.pop();
                    current->next->prev = current;
                }
            }
            return head;
        }
};



