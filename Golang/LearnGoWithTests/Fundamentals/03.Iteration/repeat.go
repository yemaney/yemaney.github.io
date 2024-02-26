package iteration

import "strings"

// returns a string of characters repeated count times
func Repeat(characters string, count int) string {
	var repeated string
	for i := 0; i < count; i++ {
		repeated += characters
	}

	repeated = strings.Repeat(characters, count)

	return repeated

}
