package main

import "fmt"

type command interface {
	execute()
	undo()
}

type device interface {
	on()
	off()
}

type onCommand struct {
	device device
}

func newOnCommand(device device) *onCommand {
	return &onCommand{
		device: device,
	}
}

func (c *onCommand) execute() {
	c.device.on()
}

func (c *onCommand) undo() {
	c.device.off()
}

type offCommand struct {
	device device
}

func newOffCommand(device device) *offCommand {
	return &offCommand{
		device: device,
	}
}

func (c *offCommand) execute() {
	c.device.off()
}

func (c *offCommand) undo() {
	c.device.off()
}

type Tv struct {
	isRunning bool
}

func newTv() device {
	return &Tv{isRunning: false}
}

func (tv *Tv) on() {
	tv.isRunning = true
	fmt.Println("Turning tv on")
}

func (tv *Tv) off() {
	tv.isRunning = false
	fmt.Println("Turning tv off")
}

type button struct {
	command command
}

func newButton(command command) command {
	return &button{command: command}
}

func (b *button) execute() {
	b.command.execute()
}

func (b *button) undo() {
	b.command.execute()
}

func main() {
	tv := newTv()

	onCommand := newOnCommand(tv)
	offCommand := newOffCommand(tv)

	onButton := button{
		command: onCommand,
	}

	offButton := button{
		command: offCommand,
	}

	onButton.execute()
	offButton.execute()
}
