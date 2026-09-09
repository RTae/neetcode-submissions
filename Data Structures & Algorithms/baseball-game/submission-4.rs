impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut res = 0;
        let mut track_score: Vec<i32> = Vec::new();
        
        for ops in operations {
            if ops == "+" {
                let tmp = track_score[track_score.len() - 1] + 
                          track_score[track_score.len() - 2];
                track_score.push(tmp);
                res += tmp;
            } else if ops == "D" {
                let tmp = track_score[track_score.len() - 1] * 2;
                track_score.push(tmp);
                res += tmp;
            } else if ops == "C" {
                let tmp = track_score.pop().unwrap();
                res -= tmp;
            } else {
                let val: i32 = ops.parse().unwrap();
                track_score.push(val);
                res += val;
            }
        }
        
        res
    }
}