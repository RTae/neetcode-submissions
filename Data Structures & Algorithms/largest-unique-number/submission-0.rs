impl Solution {
    pub fn largest_unique_number(nums: Vec<i32>) -> i32 {
        let mut frequency_map = HashMap::new();
        for &num in &nums {
            *frequency_map.entry(num).or_insert(0) += 1;
        }

        let mut largest_unique = -1;
        for (&num, &freq) in &frequency_map {
            if freq == 1 && num > largest_unique {
                largest_unique = num;
            }
        }

        largest_unique
    }
}