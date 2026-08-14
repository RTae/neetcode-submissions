impl Solution {
    pub fn can_permute_palindrome(s: String) -> bool {
        let mut set = HashSet::new();
        for b in s.bytes() {
            if !set.insert(b) {
                set.remove(&b);
            }
        }
        return set.len() <= 1
    }
}
