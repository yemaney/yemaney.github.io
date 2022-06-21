package greet

import (
	"fmt"
	"io"
	"os"
)

// takes a writer that implements the Writer interface and string name
//
// prints a message "Hello, name"
func Greet(writer io.Writer, name string) {
	fmt.Fprintf(writer, "Hello, %s", name)
}

// passes os.Stdout as the writer to Greet function
//
// prints to the command line
func CommandLineGreet() {
	Greet(os.Stdout, "Elodie")
}
