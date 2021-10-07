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
  }

  public getLogs(): any[] {
    return this.logs;
  }
}

// Implementation of Logger class.
class FirstLogger {
  private logger: Logger;

  constructor() {
    this.logger = Logger.getInstance();
  }

  public displayMessage() {
    this.logger.debug('Hello world from first logger.');
  }
}

// Implementation of Logger class.
class SecondLogger {
  private logger: Logger;

  constructor() {
    this.logger = Logger.getInstance();
  }

  public displayMessage() {
    this.logger.debug('Hello world from second logger.');
  }
}

let firstLoggerInstance = new FirstLogger();
firstLoggerInstance.displayMessage();

let secondLoggerInstance = new SecondLogger();
secondLoggerInstance.displayMessage();

let logger = Logger.getInstance();
console.log(logger.getLogs());
