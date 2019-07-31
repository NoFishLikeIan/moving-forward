package main

import "syscall/js"

func RegisterFunction(funcName string, randomfunc func(i []js.Value)) {
	js.Global().Set(funcName, js.NewCallBack(randomfunc))
}

func main() {
	println("Oak Framework Initialized")
}
