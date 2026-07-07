class Node {
    public:
        int val;
        Node* next = nullptr;
        Node* prev = nullptr;
        Node(int v) : val(v) {}
};

class MyStack {
public:
    Node* head;
    Node* curr;
    MyStack() {
        head = new Node(-1);
        curr = head;
    }
    
    void push(int x) {
        Node* newNode = new Node(x);
        newNode->prev = curr;
        curr->next = newNode;
        curr = newNode;
    }
    
    int pop() {
        if(curr->prev == nullptr) return -1;

        Node* toDelete = curr;
        int valCurr = toDelete->val;
        curr = toDelete->prev;

        delete toDelete;

        return valCurr;
    }
    
    int top() {
        if(head->next == nullptr) return -1;

        return curr->val;
    }
    
    bool empty() {
        return curr == head;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */