package main

import "strings"

func defangIPaddr(address string) string {
	return strings.Replace(address, ".", "[.]", -1)
}

func main() {
	s := defangIPaddr("127.0.0.1")
	println(s)
}
