package main

import "fmt"

type IStrategy interface {
	execute()
}

type ByBus struct{}

func newByBus() IStrategy {
	return &ByBus{}
}

func (bb *ByBus) execute() {
	fmt.Println("By bus strategy executed")
}

type ByCycle struct{}

func newByCycle() IStrategy {
	return &ByCycle{}
}

func (bb *ByCycle) execute() {
	fmt.Println("By Cycle strategy executed")
}

type IContext interface {
	setStrategy(strategy IStrategy)
	execute()
}

type Context struct {
	strategy IStrategy
}

func newContext() IContext {
	return &Context{}
}

func (c *Context) setStrategy(strategy IStrategy) {
	c.strategy = strategy
}

func (c *Context) execute() {
	c.strategy.execute()
}

func main() {
	context := newContext()
	bus := newByBus()

	context.setStrategy(bus)
	context.execute()
}
