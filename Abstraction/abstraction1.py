from abc import abstractmethod, ABC
class Whatsapp(ABC):
    @abstractmethod
    def post(self):
        pass
    @abstractmethod
    def comment(self):
        pass
    @abstractmethod
    def likes(self):
        pass

class Story(Whatsapp):
    def post(self):
        print('setting timer for 24hr')
    def comment(self):
        print("showing top 2 recent comments..")
    def likes(self):
        print("showing top 2 liked profiles..")

class ImagePost(Whatsapp):
    def post(self):
        print("No timer!!")
        print("Shareable to other apps..")
    def comment(self):
        print("statically show 2-3 comments..")
    def likes(self):
        print("display liked by.. notification")
        print("show likes count")

story1 = Story()
story1.post()
story1.likes()
print()
image1 = ImagePost()
image1.likes()
image1.post()