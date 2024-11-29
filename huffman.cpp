
#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

struct Node {
    char character;
    int frequency;
    Node* left;
    Node* right;

    Node(char ch, int freq) : character(ch), frequency(freq), left(nullptr), right(nullptr) {}
};

struct Compare {
    bool operator()(Node* left, Node* right) {
        return left->frequency > right->frequency;
    }
};

void generateHuffmanCodes(Node* root, const string& str, unordered_map<char, string>& huffmanCodes) {
    if (!root) return;

    if (root->left == nullptr && root->right == nullptr) {
        huffmanCodes[root->character] = str;
    }

    generateHuffmanCodes(root->left, str + "0", huffmanCodes);
    generateHuffmanCodes(root->right, str + "1", huffmanCodes);
}

Node* buildHuffmanTree(const string& text) {
    unordered_map<char, int> frequencyMap;

    for (char ch : text) {
        frequencyMap[ch]++;
    }

    priority_queue<Node*, vector<Node*>, Compare> minHeap;

    for (const auto& pair : frequencyMap) {
        minHeap.push(new Node(pair.first, pair.second));
    }

    while (minHeap.size() > 1) {
        Node* left = minHeap.top(); minHeap.pop();
        Node* right = minHeap.top(); minHeap.pop();

        Node* newNode = new Node('\0', left->frequency + right->frequency);
        newNode->left = left;
        newNode->right = right;
        minHeap.push(newNode);
    }

    return minHeap.top();
}


void printHuffmanCodes(const unordered_map<char, string>& huffmanCodes, const unordered_map<char, int>& frequencyMap) {
    cout << "Character | Frequency | Huffman Code" << endl;
    cout << "-------------------------------------" << endl;
    for (const auto& pair : huffmanCodes) {
        cout << "    " << pair.first << "     |    " << frequencyMap.at(pair.first) << "     |    " << pair.second << endl;
    }
}

int main() {
    string text = "ABRACADABRA";
    Node* root = buildHuffmanTree(text);

    unordered_map<char, string> huffmanCodes;
    unordered_map<char, int> frequencyMap;

 
    for (char ch : text) {
        frequencyMap[ch]++;
    }

    generateHuffmanCodes(root, "", huffmanCodes);
    printHuffmanCodes(huffmanCodes, frequencyMap);

    return 0;
}
