package shapes

import "math"

// shape interface
type Shape interface {
	Area() float64
}

// struct representing a rectangle
type Rectangle struct {
	Width  float64
	Height float64
}

// struct representing a circle
type Circle struct {
	Radius float64
}

//struct for representing a triangle
type Triangle struct {
	Base   float64
	Height float64
}

// given a width and height, calculate the perimeter of a rectangle
func Perimeter(rectangle Rectangle) float64 {
	return 2 * (rectangle.Width + rectangle.Height)
}

// given a width and height, calculate the area of a rectangle
func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

// given a radius, calculate the area of a circle
func (c Circle) Area() float64 {
	return math.Pi * c.Radius * c.Radius
}

// given a base and height, calculate the area of a triangle
func (t Triangle) Area() float64 {
	return t.Base * t.Height * 0.5
}
