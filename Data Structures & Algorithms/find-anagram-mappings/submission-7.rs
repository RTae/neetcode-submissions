impl Solution {
    pub fn anagram_mappings(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut value_to_pos = HashMap::new();
        // Convert mapping from value to pos in nums
        for (i, &num) in nums2.iter().enumerate() {
            value_to_pos.insert(num, i as i32);
        }

        // then map back with nums1
        let mut mapping = vec![0i32; nums1.len()];
        for (i, &num) in nums1.iter().enumerate() {
            mapping[i] = value_to_pos[&num];
        }

        return mapping
    }
}
