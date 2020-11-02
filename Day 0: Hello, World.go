package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	fmt.Println("Hello, World.")
	io.Copy(os.Stdout, os.Stdin)
}
