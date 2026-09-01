impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut prefix = strs[0].clone();
        for i in 1..strs.len() {
            let mut j = 0;
            let s = strs[i].as_bytes();
            let p = prefix.as_bytes();
            while j < p.len().min(s.len()) {
                if p[j] != s[j] {
                    break;
                }
                j += 1;
            }
            prefix = prefix[..j].to_string();
        }
        prefix
    }
}