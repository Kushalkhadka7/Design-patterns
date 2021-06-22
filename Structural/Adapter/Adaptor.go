package main

import "fmt"

type target struct{}
type itarget interface {
	request() string
}

func newTarget() itarget {
	return &target{}
}

func (t *target) request() string {
	return "Default behavior"
}

type adapted struct{}
type iadapted interface {
	specificRequest() string
}

func newAdapted() iadapted {
	return &adapted{}
}

func (t *adapted) specificRequest() string {
	return "Specific behavior"
}

type Adaptor struct {
	target itarget
}

func (a *Adaptor) request(adapted iadapted) string {
	result := adapted.specificRequest()

	return result
}

func main() {
	target := newTarget()
	fmt.Println(target.request())

	adapted := newAdapted()
	fmt.Println(adapted.specificRequest())

	adaptor := &Adaptor{
		target: target,
	}

	adaptor.request(adapted)
}
