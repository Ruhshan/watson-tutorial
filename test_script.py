from watson import search as watson
from watsontutapp.models import Blogger, BlogPost

import time

s=time.time()
search_results = watson.search("Provident cum necessitatibus omnis")
e=time.time()

# print(search_results)
# for result in search_results:
#     print(result.title)
print(len(search_results))
print(e-s)
from django.db.models import Q
from watsontutapp.models import Blogger, BlogPost

s=time.time()
#query = Blogger.objects.filter(Q(first_name__icontains="test alias"))
query = BlogPost.objects.filter(content__contains="Provident cum necessitatibus omnis")
print(len(query))
e=time.time()
print(e-s)
