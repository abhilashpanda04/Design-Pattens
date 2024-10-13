#Bridge Pattern
class Device:
    def power_on(self):
        pass

class TV(Device):
    def power_on(self):
        print("TV is ON")

class RemoteControl:
    def __init__(self, device):
        self.device = device

    def press_power(self):
        self.device.power_on()

# Usage
tv = TV()
remote = RemoteControl(tv)
remote.press_power()  
