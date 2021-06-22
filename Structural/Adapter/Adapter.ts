class Target {
  public request(): string {
    return `Default behavior.`;
  }
}

class Adapted {
  public specificRequest(): string {
    return `request to adapt.`;
  }
}

class Adaptor extends Target {
  private adapted: Adapted;

  constructor(adapted: Adapted) {
    super();
    this.adapted = adapted;
  }

  public request(): string {
    const result = this.adapted.specificRequest();
    // Do some modification here.

    return result;
  }
}

let target = new Target();
console.log(target.request());

let adaptor = new Adaptor(new Adapted());
console.log(adaptor.request());
