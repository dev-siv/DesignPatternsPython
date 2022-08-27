from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError
    
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        pass

# What if we have a printer that can only print but cannot fax or scan?
class OldFashionedPrinter(Machine):
    def print(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        raise NotImplementedError("Printer cannot scan!")


# to mitigate the above problem we can use the ISP pattern
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def fax(self, document):
        pass

class MultiFunctionMachine(Printer, Scanner, Fax):
    def print(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        pass


# now we can use the MultiFunctionMachine to print and fax documents
class OldFashionedPrinter(Printer):
    def print(self, document):
        pass

class OldFashionedScanner(Scanner):
    def scan(self, document):
        pass

class OldFashionedFax(Fax):
    def fax(self, document):
        pass


