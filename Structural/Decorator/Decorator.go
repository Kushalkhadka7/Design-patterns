package main

import "fmt"

type pizza struct {
	price int
	name  string
}

type IPizza interface {
	getPrice() int
	getName() string
}

func newPizza(name string, price int) IPizza {
	return &pizza{
		name:  name,
		price: price,
	}
}

func (p *pizza) getPrice() int {
	return 100
}

func (p *pizza) getName() string {
	return p.name
}

// Veg pizza.
type vegPizza struct {
	pizza IPizza
}

func newVegPizza(pizza IPizza) IPizza {
	return &vegPizza{
		pizza: pizza,
	}
}

func (p *vegPizza) getPrice() int {
	return p.pizza.getPrice() + 100
}

func (p *vegPizza) getName() string {
	return fmt.Sprintf("%s %s", p.pizza.getName(), "Vegetable")
}

func main() {
	pizza := newPizza("famous pizza", 100)
	fmt.Println(pizza.getName())

	vegPizza := newVegPizza(pizza)
	fmt.Println(vegPizza.getName())
}
