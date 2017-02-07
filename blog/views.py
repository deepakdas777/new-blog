from django.shortcuts import render_to_response
from blog.models import Post
# Create your views here.
def tagpage(request,tag):
    Posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html",{"Posts":Posts,"tag":tag})