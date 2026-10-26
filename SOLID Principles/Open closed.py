# Open for extension closed for modification
from abc import ABC, abstractmethod
class Content(ABC):
    @abstractmethod
    def play(self):
        pass

class Movies(Content):
    def play(self):
        print("Playing Movie..")

class WebSeries(Content):
    def play(self):
        print("Playing web series..")

movie = Movies()
web_series = WebSeries()

movie.play()
web_series.play()