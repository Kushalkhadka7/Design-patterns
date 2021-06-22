class RemoteControl {
  public device: Device;

  constructor(device: Device) {
    this.device = device;
  }

  public togglePower() {
    if (this.device.isEnabled) {
      this.device.disable();
    } else {
      this.device.enable();
    }
  }
}

class AdvanceRemoteControl extends RemoteControl {
  public device: Device;

  constructor(device: Device) {
    super(device);
    this.device = device;
  }
  public mute() {
    super.device.setVolume(0);
  }
}

interface Device {
  disable(): void;
  enable(): void;
  setVolume(arg: number): void;
}

class Device implements Device {
  private isEnabled: boolean = false;

  public disable(): void {
    console.log('hello world');
  }

  public enable(): void {
    console.log('hello world');
  }
}

class Television extends Device {
  constructor() {
    super();
  }

  public disable(): void {
    console.log('hello world');
  }
  public enable(): void {
    console.log('hello world');
  }

  public setVolume(arg: number = 0): void {
    console.log('hello world');
  }
}
