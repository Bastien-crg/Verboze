
class Environment:

    def __init__(self, enclosing = None):
        self.values:dict[str,any] = dict()
        self.enclosing:Environment = enclosing


    def define(self, name:str, value:any):
        self.values[name] = value

    def assign(self, name:str, value:any):
        if name in self.values:
            self.values[name] = value
            return

        if self.enclosing is not None:
            self.enclosing.assign(name, value)

        raise RuntimeError()

    def get(self,name:str):
        if name in self.values:
            return self.values[name]

        if self.enclosing is not None:
            return self.enclosing.get(name)

        raise RuntimeError()

    def is_in(self,name:str):
        return name in self.values


