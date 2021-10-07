package main

import "fmt"

type Logger struct{}

func newLogger() *Logger {
	return &Logger{}
}

var logger *Logger

func getLogger() *Logger {
	if logger == nil {
		logger = newLogger()
	}

	return logger
}

func main() {
	for i := 0; i < 30; i++ {
		go getLogger()
	}

	fmt.Scanln()
}
