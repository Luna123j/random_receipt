from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('polls/index.html')
    # food = {'name1': "sandwitch",
    #         'name2': 'chicken',
    #         'name3': 'ham',
    #         'name4': 'beef',
    #         'name5': 'pork',
    #         'name6': 'vegetable',
    #         'name7': 'fish',
    #         'name8': 'seaffood',
    #         }

    food = ["sandwitch",'chicken','ham','beef','pork','vegetable','fish','seaffood']
    return HttpResponse(template.render({"food": food},request))
