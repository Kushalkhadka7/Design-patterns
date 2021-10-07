package main

import "fmt"

type IListener interface {
	update()
}

type IPublisher interface {
	notify()
	subscribe(listener IListener)
	unSubscribe(listener IListener)
}

// Publisher.
type Publisher struct {
	listerners []IListener
}

func newPublisher() IPublisher {
	return &Publisher{listerners: make([]IListener, 0)}
}

func (p *Publisher) subscribe(listener IListener) {
	p.listerners = append(p.listerners, listener)

}

func (p *Publisher) unSubscribe(listener IListener) {
	p.listerners = p.listerners[:len(p.listerners)-1]
}

func (p *Publisher) notify() {
	for _, listener := range p.listerners {
		listener.update()
	}
}

// Logging listener.

type LoggingListener struct {
	message string
}

func newLoggingListener(message string) IListener {
	return &LoggingListener{
		message: message,
	}
}

func (ll *LoggingListener) update() {
	fmt.Printf("Logging listener: %s \n", ll.message)
}

// Email Alert.
type EmailAlert struct {
	message string
}

func newEmailAlert(message string) IListener {
	return &EmailAlert{
		message: message,
	}
}

func (ll *EmailAlert) update() {
	fmt.Printf("Logging listener: %s \n", ll.message)
}

// Event.
type Event struct {
	publisher IPublisher
}

func newEvent(publisher IPublisher) *Event {
	return &Event{
		publisher: publisher,
	}
}

func (e *Event) openFile() {
	e.publisher.notify()
}

func main() {
	publisher := newPublisher()
	event := newEvent(publisher)
	logger := newLoggingListener("hello")
	email := newEmailAlert("hello")

	event.publisher.subscribe(logger)
	event.publisher.subscribe(email)

	event.openFile()
}
