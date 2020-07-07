from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from markdown2 import Markdown
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    markdowner = Markdown()
    acumulador = []
    if util.get_entry(title) == None:
        for titles in util.list_entries():
            if titles[0:len(title)].lower() == title.lower():
                acumulador.append(titles)
        if acumulador:
            return render(request, "encyclopedia/index.html", {
                "entries": acumulador
            })
        raise Http404("Title does not exist")
    markdown = markdowner.convert(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown,
        "title": title,
    })

def search(request):
    query = request.POST.get('q','')
    if query:
        return HttpResponseRedirect(reverse('wiki', args=(query,)))
    else:
        return HttpResponseRedirect(reverse('index'))

def create_entry(request):
    new_title = request.POST.get('title')
    content = request.POST.get('content')
    entries = [x.lower() for x in util.list_entries()]
    if new_title:
        if new_title.lower() in entries:
            raise Http404("Title does not exist")
        else:
            util.save_entry(new_title, content)
            return HttpResponseRedirect(reverse('wiki', args=(new_title,)))
    return render(request, "encyclopedia/new-entry.html")

def edit(request, title):
    content = request.POST.get('content')
    if content:
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse('wiki', args=(title,)))
    return render(request, "encyclopedia/edit-entry.html", {
        "title": title
    })

def randompick(request):
    random_title = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse('wiki', args=(random_title,)))
