from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me!'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()       #this splits the words and makes a list of them

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increment
            worddictionary[word] += 1
        else:
            #add the word to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext' : fulltext, 'count':len(wordlist), 'sortedwords' : sortedwords})


def about(request):
    return render(request, 'about.html')
