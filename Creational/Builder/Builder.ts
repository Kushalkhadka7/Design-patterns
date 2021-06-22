interface Builder {
  buildPartA(): void;
  buildPartB(): void;
  buildPartC(): void;
}

class MainProduct {
  public parts: string[] = [];

  public listParts(): void {
    console.log(`Product parts: ${this.parts.join(', ')}\n`);
  }
}

class BuilderA implements Builder {
  private product: MainProduct;

  constructor() {
    this.reset();
  }

  public reset(): void {
    this.product = new MainProduct();
  }

  public buildPartA(): void {
    this.product.parts.push('PartA1');
  }

  public buildPartB(): void {
    this.product.parts.push('PartB1');
  }

  public buildPartC(): void {
    this.product.parts.push('PartC1');
  }

  public buildProduct(): MainProduct {
    const result = this.product;
    this.reset();
    return result;
  }
}

class Director {
  private builder: Builder;

  public setBuilder(builder: Builder): void {
    this.builder = builder;
  }

  public buildProduct(): void {
    this.builder.buildPartA();
    this.builder.buildPartB();
    this.builder.buildPartB();
  }
}

function main() {
  const director = new Director();
  const builder = new BuilderA();
  director.setBuilder(builder);
}
