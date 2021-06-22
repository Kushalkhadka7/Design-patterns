/**
 * Singleton logger
 */
class Logger {
  private logs: any[];
  private static instance: Logger;

  private constructor() {}

  public static getInstance(): Logger {
    if (!Logger.instance) {
      Logger.instance = new Logger();
    }

    return Logger.instance;
  }

  public debug(message: any) {
    this.logs.push(message);
    console.log(`[DEBUG]: ${message}`);
  }

  public getLogs(): any[] {
    return this.logs;
  }
}

class FirstImplementation {
  private logger: Logger;

  constructor() {
    this.logger = Logger.getInstance();
  }

  public displayMessage() {
    this.logger.debug('hello world from first.');
  }
}

class SecondImplementation {
  private logger: Logger;

  constructor() {
    this.logger = Logger.getInstance();
  }

  public displayMessage() {
    this.logger.debug('hello world from second.');
  }
}

let firstInstance = new FirstImplementation();
firstInstance.displayMessage();

let secondInstance = new SecondImplementation();
secondInstance.displayMessage();

let logger = Logger.getInstance();
console.log(logger.getLogs());
