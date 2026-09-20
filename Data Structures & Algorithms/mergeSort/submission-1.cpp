// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<Pair> mergeSort(vector<Pair>& pairs) {
        mergeSortHelper(pairs, 0, pairs.size()-1);
    }

    void mergeSortHelper(vector<Pair>& pairs, int s, int e) {
        if (e-s-1 <= 1) { // it mean we have only one pair
            return;
        }

        int m = (e+s)/2;

        mergeSortHelper(paris, s, m);
        mergeSortHelper(paris, m+1, e);

        merge(paris, s, m, e);
    }

    void merge(vector<Pair>& arr, int s, int m, int e) {
        vector<Pair> L(arr.begin()+s, arr.begin()+m+1);
        vector<Pair> R(arr.begin()+m+1, arr.begin()+e+1);

        int i = 0; // L
        int j = 0; // R
        int k = s; // arr

        // Merge L and R ino arr
        while(i < L.size() && j < R.size()) {
            if(L[i].key <= R[j].key) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        // Loop remain element from L and R
        while(i<L.size()) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while(j<R.size()) {
            arr[k] = L[j];
            j++;
            k++;
        }
    }
};
