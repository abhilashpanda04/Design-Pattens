#builder design pattern

class Computer:
    def __init__(self):
        self.name=None
        self.cpu=None
        self.gpu=None
        
    def __repr__(self):
        return f"computer with {self.name},{self.gpu} and {self.cpu} is created"
        

class ComputerBuilder:
    def __init__(self):
        self.computer=Computer()
        
    def set_name(self,name):
        self.computer.name=name
        return self    
        
    def set_cpu(self,cpu):
        self.computer.cpu=cpu
        return self
        
    def set_gpu(self,gpu):
        self.computer.gpu=gpu
        return self
        
    def build(self):
        return self.computer


if __name__=="__main__":
    builder=ComputerBuilder()
    computer=builder.set_name("razor").set_cpu("intel").set_gpu("rtx 3039").build()
    
    print(computer)
