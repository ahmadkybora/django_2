from django.shortcuts import get_object_or_404, render
from .models import Blog
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import logging

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# logger = logging.getLogger("info")
logger = logging.getLogger('django.request')

def index(request):

    # logger.info('something')
    blogs = Blog.objects.all()
    # logger.info("is: ", request)
    template = loader.get_template("index.html")
    context = {
        "blogs": blogs
    }
    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == "POST":
        logger.info("o", request.POST)
        blog = Blog()
        blog.title = "12"
        blog.description = "12"
        blog.save()
        blogs = Blog.objects.all()
        return render(request, "index.html", {"blogs": blogs})

def detail(request, id):
    logger.info("request is: ", request )
    # logger.info('something')
    # logger = logging.getLogger()
    # logger.setLevel(logging.INFO)para
    # logger.info("is: ", request)
    blog = get_object_or_404(Blog, pk=id)
    return render(request, "detail.html", {"blog": blog})

def update(request, id):
    logger.info("update is: ", request )
    # logger.info("is: ", request)
    blog = get_object_or_404(Blog, pk=id)
    blog.title = "s"
    blog.description = "a"
    blog.save()
    blogs = Blog.objects.all()
    return render(request, "index.html", {"blogs": blogs})
    # logger.info("is: ", request)
    # template = loader.get_template("index.html")
    # context = {
    #     "blogs": blogs
    # }
    # return HttpResponse(template.render(context, request))
    # return HttpResponseRedirect(reverse("blogs"))