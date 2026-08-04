impl Solution {
    pub fn confusing_number(n: i32) -> bool {
        let invert_map: HashMap<i32, i32> = [
            (0,0), (1,1), (6,9), (8,8), (9,6),
        ].iter().cloned().collect();
        let mut n_copy = n;
        let mut rotated_number = 0;

        while n_copy > 0 {
            // Extract number
            let res = n_copy % 10;
            match invert_map.get(&res) {
                Some(&inverted) => {
                    rotated_number = rotated_number*10 + inverted
                }
                None => return false,
            }
            n_copy /= 10;
        }

        rotated_number != n
    }
}
