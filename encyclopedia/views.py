from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    if util.get_entry(title) == None:
        raise Http404("Title does not exist")
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "title": title,
    })

def search(request):
    query = request.POST.get('q','')
    if query:
        return HttpResponseRedirect(reverse('wiki', args=(query,)))
    else:
        return HttpResponseRedirect(reverse('index'))
