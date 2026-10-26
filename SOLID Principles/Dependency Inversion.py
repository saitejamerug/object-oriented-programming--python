from abc import ABC, abstractmethod
class Storage(ABC):
    @abstractmethod
    def save(self):
        pass
class CloudStorage(Storage):
    def save(self):
        print("Saving on Cloud Storage")

class LocalStorage(Storage):
    def save(self):
        print("Saving on Local Storage")

class Netflix:
    def __init__(self, storage):
        self.storage = storage
    def video(self):
        self.storage.save()

Netflix(CloudStorage()).video()
Netflix(LocalStorage()).video()