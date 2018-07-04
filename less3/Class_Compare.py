from abc import ABC, abstractmethod
class Compare(ABC):
    @abstractmethod
    def do_compare(self,obj):
        pass


    def compere(self,obj):
        if isinstance(obj,self):   #если обьект того же класса что и текущий
            return self.do_compare(obj)
        else:
            raise Exception("Sorry, try later")


