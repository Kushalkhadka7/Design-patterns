interface Handler {
  next(handler: Handler): Handler;
  operation(request: string): string;
}

abstract class BaseHandler implements Handler {
  private handler: Handler;

  public next(handler: Handler): Handler {
    this.handler = handler;

    return handler;
  }

  public operation(request: string): string {
    if (this.handler) {
      return this.handler.operation(request);
    }

    return null;
  }
}

class MonkeyHandler extends BaseHandler {
  public operation(request: string): string {
    if (request === 'Banana') {
      return 'I am a monkey and i love banana';
    }

    super.operation(request);
  }
}

class DogHandler extends BaseHandler {
  public operation(request: string): string {
    if (request === 'meat') {
      return 'I am a dog and i love meat';
    }

    super.operation(request);
  }
}

const monkey = new MonkeyHandler();
const dog = new DogHandler();

monkey.next(dog);
