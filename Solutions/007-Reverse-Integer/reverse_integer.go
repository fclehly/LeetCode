package main

import "math"

func reverse(x int) int {
	ans := 0
	max, min := 1<<31-1, -1<<31
	for x != 0 {
		t := x % 10
		x = x / 10
		ans = ans*10 + t
		if ans > max || ans < min {
			return 0
		}
	}
	return ans
}

func main() {
	input := []int{123, -123, 120, int(math.Pow(2, 31)) - 1, -1 << 31, 1534236469}
	for i, x := range input {
		println(i, x, reverse(x))
	}
	println(9646324351)
	println(1 << 31)
}
