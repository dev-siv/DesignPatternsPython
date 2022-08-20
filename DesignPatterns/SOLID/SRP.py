import os


class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.counter = 0

    def add_entries(self, text):
        self.counter += 1
        self.entries.append(f"{self.counter}: {text}")

    def remove_entries(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # now SRP is broken by implementation of the below method
    
    """
    Apart from adding entries and deleting entries journal has now taken the 
    responsibility of persistence!
    """
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()
    
    def load(self, filename):
        # file = open(filename, "r")
        pass

    def load_from_web(self, uri):
        pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entries("First line")
    j.add_entries("Second line")
    print(f"Journal entries: \n{j}")
    filename = "journal.txt"
    PersistenceManager.save_to_file(j, filename)
