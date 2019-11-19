package main

func numJewelsInStones(J string, S string) int {
	dict := make(map[rune]int)
	for _, v := range J {
		dict[v] = 0
	}
	var count int = 0
	for _, v := range S {
		_, ok := dict[v]
		if ok {
			count++
		}
	}
	return count
}

func main() {
	j, s := "a", "aazzzz"
	var count int = numJewelsInStones(j, s)
	println(count)
}
