impl Solution {
    pub fn calculate_time(keyboard: String, word: String) -> i32 {
        let mut keyboard_map = [0i32; 26];

        for (i, c) in keyboard.bytes().enumerate() {
            keyboard_map[(c - b'a') as usize] = i as i32
        }

        let mut prev = 0i32;
        let mut result = 0i32;

        for c in word.bytes() {
            let idx = keyboard_map[(c-b'a') as usize];
            result += (prev-idx).abs();
            prev = idx;
        }

        return result
    }
}
