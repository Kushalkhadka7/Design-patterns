// Product interface.
interface Product {
  operation(): string;
}

/**
 * Main creator class.
 */
abstract class Creator {
  public abstract factoryMethod(): Product;

  public someOperation(): string {
    const product = this.factoryMethod();

    return `Creator code worked with ${product.operation()}`;
  }
}

/**
 * Creator A.
 */
class CreatorA extends Creator {
  public factoryMethod(): Product {
    return new ProductA();
  }
}

/**
 * Creator B.
 */
class CreatorB extends Creator {
  public factoryMethod(): Product {
    return new ProductB();
  }
}

/**
 * Product A will be created by creator A.
 */
class ProductA implements Product {
  public operation(): string {
    return `Created by creatorA`;
  }
}

/**
 * Product A will be created by creator A.
 */
class ProductB implements Product {
  public operation(): string {
    return `Created by creatorA`;
  }
}

function main(creator: Creator) {
  console.log(creator.someOperation());
}

main(new CreatorA());
