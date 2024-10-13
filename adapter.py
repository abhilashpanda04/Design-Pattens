class EuropeanPlug:
    def plugin(self):
        print( "european plug connected")
        
class PlugAdapter:
    def __init__(self,europeanplug):
        self.europeanplug=europeanplug
    
    def connect(self):
        self.europeanplug.plugin()

plug=EuropeanPlug()
adapter=PlugAdapter(plug)
adapter.connect()
