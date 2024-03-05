#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;

// Function prototypes
pair<int, double> bubbleSort(vector<int>&);
pair<int, double> selectionSort(vector<int>&);
pair<int, double> insertionSort(vector<int>&);
pair<int, double> mergeSort(vector<int>&, int, int);
pair<int, double> quickSort(vector<int>&, int, int);
pair<int, double> heapify(vector<int>&, int, int);
pair<int, double> heapSort(vector<int>&);
vector<int> countingSort(vector<int>&);

int main() {
    vector<int> arr = {4, 2, 2, 8, 3, 3, 1};
    
    // Testing each sorting algorithm
    pair<int, double> result;
    
    result = bubbleSort(arr);
    cout << "Bubble Sort: " << result.first << " comparisons, " << result.second << " seconds" << endl;
    
    result = selectionSort(arr);
    cout << "Selection Sort: " << result.first << " comparisons, " << result.second << " seconds" << endl;
    
    result = insertionSort(arr);
    cout << "Insertion Sort: " << result.first << " comparisons, " << result.second << " seconds" << endl;
    
    result = mergeSort(arr, 0, arr.size() - 1);
    cout << "Merge Sort: " << result.first << " comparisons, " << result.second << " seconds" << endl;
    
    result = quickSort(arr, 0, arr.size() - 1);
    cout << "Quick Sort: " << result.first << " comparisons, " << result.second << " seconds" << endl;
    
    result = heapSort(arr);
    cout << "Heap Sort: " << result.first << " comparisons, " << result.second << " seconds" << endl;
    
    vector<int> sorted_arr = countingSort(arr);
    cout << "Counting Sort: Sorted array: ";
    for (int num : sorted_arr) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}

pair<int, double> bubbleSort(vector<int>& arr) {
    clock_t start_time = clock();
    int ctr = 0;
    int n = arr.size();
    
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            ctr++;
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
    
    double execution_time = static_cast<double>(clock() - start_time) / CLOCKS_PER_SEC;
    return {ctr, execution_time};
}

pair<int, double> selectionSort(vector<int>& arr) {
    clock_t start_time = clock();
    int ctr = 0;
    int n = arr.size();
    
    for (int i = 0; i < n - 1; i++) {
        int min_index = i;
        for (int j = i + 1; j < n; j++) {
            ctr++;
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        swap(arr[i], arr[min_index]);
    }
    
    double execution_time = static_cast<double>(clock() - start_time) / CLOCKS_PER_SEC;
    return {ctr, execution_time};
}

pair<int, double> insertionSort(vector<int>& arr) {
    clock_t start_time = clock();
    int ctr = 0;
    int n = arr.size();
    
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            ctr++;
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    
    double execution_time = static_cast<double>(clock() - start_time) / CLOCKS_PER_SEC;
    return {ctr, execution_time};
}

pair<int, double> mergeSort(vector<int>& arr, int low, int high) {
    clock_t start_time = clock();
    int ctr = 0;
    if (low < high) {
        int mid = low + (high - low) / 2;
        pair<int, double> left = mergeSort(arr, low, mid);
        pair<int, double> right = mergeSort(arr, mid + 1, high);
        ctr += left.first + right.first;
        
        vector<int> merged(high - low + 1);
        int i = low, j = mid + 1, k = 0;
        while (i <= mid && j <= high) {
            ctr++;
            if (arr[i] <= arr[j]) {
                merged[k++] = arr[i++];
            } else {
                merged[k++] = arr[j++];
            }
        }
        while (i <= mid) {
            merged[k++] = arr[i++];
        }
        while (j <= high) {
            merged[k++] = arr[j++];
        }
        for (int i = low; i <= high; i++) {
            arr[i] = merged[i - low];
        }
    }
    
    double execution_time = static_cast<double>(clock() - start_time) / CLOCKS_PER_SEC;
    return {ctr, execution_time};
}

pair<int, double> quickSort(vector<int>& arr, int low, int high) {
    clock_t start_time = clock();
    int ctr = 0;
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j <= high - 1; j++) {
            ctr++;
            if (arr[j] < pivot) {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]);
        int pi = i + 1;
        
        pair<int, double> left = quickSort(arr, low, pi - 1);
        pair<int, double> right = quickSort(arr, pi + 1, high);
        ctr += left.first + right.first;
    }
    
    double execution_time = static_cast<double>(clock() - start_time) / CLOCKS_PER_SEC;
    return {ctr, execution_time};
}

pair<int, double> heapify(vector<int>& arr, int size, int i) {
    clock_t start_time = clock();
    int ctr = 0;
    int largest = i;
    int l_child = 2 * i + 1;
    int r_child = 2 * i + 2;

    if (l_child < size && arr[l_child] > arr[largest]) {
        largest = l_child;
    }
    if (r_child < size && arr[r_child] > arr[largest]) {
        largest = r_child;
    }
    if (largest != i) {
