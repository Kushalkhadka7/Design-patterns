package main

import "fmt"

type Handler interface {
	next(handler Handler)
	operation(request string)
}

type Receptionist struct {
	handler Handler
}

func newReceptionist() Handler {
	return &Receptionist{}
}

func (r *Receptionist) next(handler Handler) {
	r.handler = handler
}

func (r *Receptionist) operation(request string) {
	if r.handler != nil && request == "reception" {
		fmt.Println("Receptionist is processing payment")
	}

	r.handler.operation(request)
}

type Doctor struct {
	handler Handler
}

func newDoctor() Handler {
	return &Doctor{}
}

func (d *Doctor) next(handler Handler) {
	d.handler = handler
}

func (d *Doctor) operation(request string) {
	if d.handler != nil && request == "doctor" {
		fmt.Println("Doctor doing treatment.")
	}

	d.handler.operation(request)
}

type Medical struct {
	handler Handler
}

func newMedical() Handler {
	return &Receptionist{}
}

func (m *Medical) next(handler Handler) {
	m.handler = handler
}

func (m *Medical) operation(request string) {
	fmt.Println("Processing mediciene")
}

func main() {
	receptionist := newReceptionist()

	medical := newMedical()
	doctor := newDoctor()

	doctor.next(medical)
	doctor.operation("doctor")
	medical.next(receptionist)
}
