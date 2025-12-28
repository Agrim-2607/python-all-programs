from abc import ABC,abstractclassmethod
class vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres=n
    @abstractclassmethod
    def start(self):
        pass
    def display(self):
        print("Hi i m calling from vehicle class")   

  