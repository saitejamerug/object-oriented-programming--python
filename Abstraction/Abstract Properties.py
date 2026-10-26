# Abstract Properties
# Combine abstraction with properties: write an abstract class DataStorage (ABC) with an abstract property
# storage_type and abstract methods save(data), load(key), and delete(key). Implement FileStorage and
# MemoryStorage. Demonstrate that both are interchangeable
from abc import ABC, abstractmethod
class DataStorage(ABC):
    @property
    @abstractmethod
    def storage_type(self):
        pass
    @abstractmethod
    def save(self, data):
        pass
    @abstractmethod
    def load(self, key):
        pass
    @abstractmethod
    def delete(self, key):
        pass
class FileStorage(DataStorage):
    def save(self, data):
        print("saving data in the file..", data)
    def load(self, key):
        print("loading the data with key..", key)
    def delete(self, key):
        print("deleting the data with key..", key)
    @property
    def storage_type(self):
        return FileStorage.__name__

class MemoryStorage(DataStorage):
    def save(self, data):
        print("saving data in the file..", data)

    def load(self, key):
        print("loading the data with key..", key)

    def delete(self, key):
        print("deleting the data with key..", key)

    @property
    def storage_type(self):
        return MemoryStorage.__name__

file = FileStorage()
file.save("Hey!!")
print(file.storage_type)
mem = MemoryStorage()
mem.save("This is data!!")
print(mem.storage_type)