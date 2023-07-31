package data

import "testing"

func TestCheckValidation(t *testing.T) {
	p := &Product{SKU : "adf"}

	err := p.Validate()
	if err != nil {
		t.Fatal(err)
	}
}
