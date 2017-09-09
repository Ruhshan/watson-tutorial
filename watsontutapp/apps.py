from django.apps import AppConfig
from watson import search as watson_search

class WatsontutappConfig(AppConfig):
    name = 'watsontutapp'
    def ready(self):
        blogger_model = self.get_model("Blogger")
        blogpost_model = self.get_model("BlogPost")
        #watson_search.register(blogger_model)
        watson_search.register(blogpost_model, fields=['title', 'content'])


