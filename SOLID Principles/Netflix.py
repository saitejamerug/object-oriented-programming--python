from abc import ABC, abstractmethod
class Netflix(ABC):
    def __init__(self, username , pwd , device):
        self.username = username
        self.pwd = pwd
        self.device = device
class ContentManager(Netflix):
    def __init__(self, username, pwd, device):
        super().__init__(username, pwd, device)
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def remove(self):
        pass
class Downloadable(ABC):
    @abstractmethod
    def download(self):
        pass
class Movies(ContentManager, Downloadable):
    def play(self):
        print(f"Playing a movie for {self.username}!")
    def remove(self):
        print("Removing the movie!")
    def download(self):
        print(f"Downloading the movie on {self.device.__class__.__name__}.")

class Series(ContentManager, Downloadable):
    def play(self):
        print(f"Playing a series for {self.username}.")
    def next_episode(self):
        print("Playing next episode")
    def previous_episode(self):
        print("Playing previous episode")
    def remove(self):
        print("Removing series")
    def download(self):
        print(f"Downloading the series on {self.device.__class__.__name__}.")
class Documentary(ContentManager, Downloadable):
    def play(self):
        print("Playing a documentary!")
    def remove(self):
        print("Removing Documentary")
    def download(self):
        print(f"Downloading the Documentary on {self.device.__class__.__name__}.")
class Trailer(ContentManager):
    def play(self):
        print("Playing a trailer.")
    def remove(self):
        print("Removing Trailer")
class PaymentManager(Netflix):
    @abstractmethod
    def pay(self):
        pass
class NotificationManager(Netflix):
    @abstractmethod
    def send(self):
        pass
class Devices:
    pass
class Phone(Devices):
    def __init__(self):
        print("Logged in on phone!")
class TV(Devices):
    def __init__(self):
        print("Logged in on TV!")
class PC(Devices):
    def __init__(self):
        print("Logged in on PC!")
class Tablet(Devices):
    def __init__(self):
        print("Logged in on Tablet!")
def stream(content):
    content.play()
# stream(Movies())
# stream(Series())
# stream(Trailer())
# stream(Documentary())
movie = Movies("alice", "alice123", Phone())
movie.play()
movie.download()
series =  Series("bob", "bob123", PC())
series.play()
series.next_episode()
series.previous_episode()
series.download()