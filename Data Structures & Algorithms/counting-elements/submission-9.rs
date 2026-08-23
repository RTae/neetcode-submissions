impl Solution {
    pub fn count_elements(arr: Vec<i32>) -> i32 {
        let count_num: HashSet<i32> = arr.iter().copied().collect();
        let mut count = 0;
        for &x in &arr {
            if count_num.contains(&(x+1)) {
                count+=1;
            }
        }

        return count
    }
}
