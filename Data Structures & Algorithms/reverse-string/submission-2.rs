impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut stack: Vec<char> = s.iter().cloned().collect();
        for i in 0..s.len() {
            s[i] = stack.pop().unwrap();
        }
    }
}
