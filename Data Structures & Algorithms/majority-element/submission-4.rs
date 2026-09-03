impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut cnt = 0;

        for &num in &nums {
            if cnt == 0 {
                res = num
            }
            cnt += if num == res { 1 } else { -1 };
        }

        return res
    }
}
