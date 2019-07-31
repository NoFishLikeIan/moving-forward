package components

import (
	"syscall/js"
)

type Component interface {
	Render() string
}
type AboutComponent struct{}

var About AboutComponent

func init() {
	oak.RegisterFunction("Printing a rose", RosePrint)
}

func RosePrint(i []js.Value) {
	println("------<-------@")
}

func (a AboutComponent) Render() string {
	return `<div>
						<h2>About Component Actually Works</h2>
						<button onClick="coolFunc();">Cool Func</button>
					</div>`
}
