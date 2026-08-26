impl Solution {
    pub fn string_shift(s: String, shift: Vec<Vec<i32>>) -> String {
        let mut left_shift: i32=0;
        for m in &shift {
            if m[0] == 1 {
                left_shift -= m[1];
            } else {
                left_shift += m[1];
            }
        }
        let n = s.len() as i32;
        let left_shift = ((left_shift % n) + n) % n;
        let mut bytes = s.into_bytes();
        bytes.rotate_left(left_shift as usize);
        String::from_utf8(bytes).unwrap()
    }
}
