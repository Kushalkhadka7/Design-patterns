# Chain Of Responsibility Design Pattern

Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

In this pattern, normally each receiver contains reference to another receiver. If one object cannot handle the request then it passes the same to the next receiver and so on.

## Application

Use the Chain of Responsibility pattern when the program is expected to process different kinds of requests in various ways, but the exact types of requests and their sequences are unknown beforehand.
