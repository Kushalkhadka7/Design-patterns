# Command Design Pattern

## Overview

Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets to pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

Command pattern is a data driven design pattern and falls under behavioral pattern category. A request is wrapped under an object as command and passed to invoker object. Invoker object looks for the appropriate object which can handle this command and passes the command to the corresponding object which executes the command.

## Application

Use the Command pattern when we want to parametrize objects with operations.
