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
        return pairs;
    }

    void mergeSortHelper(vector<Pair>& pairs, int s, int e){
        // if array's length is less than 1 return
        if(e-s+1<=1){
            return;
        }

        int m = (s+e)/2; // finding center index
        mergeSortHelper(pairs, s, m);
        mergeSortHelper(pairs, m+1, e);

        merge(pairs, s, m, e);
    }

    void merge(vector<Pair>& arr, int s, int m, int e){
        // copy a data into two array
        vector<Pair> L(arr.begin()+s, arr.begin()+m+1);
        vector<Pair> R(arr.begin()+m+1, arr.begin()+e+1);

        int i=0; // L
        int j=0; // R
        int k=s; // arr

        // Merge two arrays into single array
        while(i<L.size()&&j<R.size()) {
            if (L[i].key <= R[j].key) {
                arr[k] = L[i];
                ++i;
                ++k;
            } else {
                arr[k] = R[j];
                ++j;
                ++k;
            }
        }

        // Check remain data in the array
        while(i<L.size()) {
            arr[k]=L[i];
            ++i;
            ++k;
        }
        while(j<R.size()){
            arr[k]=R[j];
            ++j;
            ++k;
        }
    }
};
