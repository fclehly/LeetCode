package main

func twoSum(nums []int, target int) []int {
	reverseMap := map[int]int{}
	for i := 0; i < len(nums); i++ {
		var index, ok = reverseMap[nums[i]]
		if ok && i != index {
			ans := []int{index, i}
			return ans
		}
		reverseMap[target-nums[i]] = i
	}
	return nil
}

func main() {
	nums := []int{3, 2, 4}
	target := 6
	var ans = twoSum(nums, target)
	for i, v := range ans {
		println(i, v)
	}
}
