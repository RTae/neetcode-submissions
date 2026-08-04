impl Solution {
    pub fn confusing_number(n: i32) -> bool {
        // There are two main condition
        // 1. it must be able to rotate
        // 2. it must not equal to orginal number
        // Create a map number first
        let invert_map: HashMap<i32, i32> = [
            (0,0), (1,1), (6,9), (8,8), (9,6),
        ].iter().cloned().collect();
        // copy pointer
        let mut n_copy = n;
        let mut rotated_number = 0;

        // we need to check the number from left to right
        // keep process number until less than zero
        while n_copy > 0 {
            // Extract number
            let res = n_copy % 10;
            match invert_map.get(&res) {
                // if found a match mean it can rotate
                Some(&inverted) => {
                    // 86
                    // ex 8 = 0*10 + 8 = 8
                    // ex 6 = 8*10 + 9 = 89
                    rotated_number = rotated_number*10 + inverted
                }
                // return false if it cannot rotate
                None => return false,
            }
            // shift left
            n_copy /= 10;
        }
        // check last condition it's a same number or not
        return rotated_number != n
    }
}
