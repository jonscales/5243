#include <iostream>
using namespace std;

// AVL Node
struct Node {
    int data;
    Node* left;
    Node* right;
    int height;
};

// Calculate the height of a node
int height(Node* node) {
    if (node == nullptr)
        return 0;
    return node->height;
}

// Get the balance factor of a node
int balanceFactor(Node* node) {
    if (node == nullptr)
        return 0;
    return height(node->left) - height(node->right);
}

// Create a new AVL node
Node* newNode(int data) {
    Node* node = new Node();
    node->data = data;
    node->left = nullptr;
    node->right = nullptr;
    node->height = 1; // new node is initially at height 1
    return node;
}

// Right rotate subtree rooted with y
Node* rightRotate(Node* y) {
    Node* x = y->left;
    Node* T2 = x->right;

    // Perform rotation
    x->right = y;
    y->left = T2;

    // Update heights
    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;

    // Return new root
    return x;
}

// Left rotate subtree rooted with x
Node* leftRotate(Node* x) {
    Node* y = x->right;
    Node* T2 = y->left;

    // Perform rotation
    y->left = x;
    x->right = T2;

    // Update heights
    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    // Return new root
    return y;
}

// Insert a new node into the AVL tree
Node* insert(Node* node, int data) {
    // Perform normal BST insertion
    if (node == nullptr)
        return newNode(data);

    if (data < node->data)
        node->left = insert(node->left, data);
    else if (data > node->data)
        node->right = insert(node->right, data);
    else // Duplicate keys are not allowed
        return node;

    // Update height of this ancestor node
    node->height = 1 + max(height(node->left), height(node->right));

    // Get the balance factor to check whether this node became unbalanced
    int balance = balanceFactor(node);

    // If node becomes unbalanced, there are 4 cases

    // Left Left Case
    if (balance > 1 && data < node->left->data)
        return rightRotate(node);

    // Right Right Case
    if (balance < -1 && data > node->right->data)
        return leftRotate(node);

    // Left Right Case
    if (balance > 1 && data > node->left->data) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Right Left Case
    if (balance < -1 && data < node->right->data) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    // If the node is already balanced, return the unchanged node pointer
    return node;
}

// Print the AVL tree in inorder traversal
void inorder(Node* root) {
    if (root != nullptr) {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}

int main() {
    Node* root = nullptr;

    // Inserting elements into the AVL tree
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    root = insert(root, 25);

    cout << "Inorder traversal of the constructed AVL tree is: ";
    inorder(root);

    return 0;
}
