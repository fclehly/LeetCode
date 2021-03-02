type NumMatrix struct {
    presum [][]int
}


func Constructor(matrix [][]int) NumMatrix {
    row, col := len(matrix), 0
    if row != 0 {
        col = len(matrix[0])
    }
    presum := make([][]int, row + 1)
    presum[0] = make([]int, col + 1)
    for i := 0; i < row; i++ {
        presum[i + 1] = make([]int, col + 1)
        // fmt.Printf("i=%d, len(presum[i + 1])=%d, col=%d\n", i, len(presum[i + 1]), col)
        for j := 0; j < col; j++ {
            // fmt.Printf("j=%d, len(presum[i])=%d\n", j, len(presum[i]))
            presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + matrix[i][j] 
        }
    }
    return NumMatrix{presum}
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    return this.presum[row2 + 1][col2 + 1] - this.presum[row2 + 1][col1] - this.presum[row1][col2 + 1] + this.presum[row1][col1]
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
