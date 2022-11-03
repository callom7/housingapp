from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404


def homePage(response):
    return render(response, "main/homePage.html", {})

def eligiblePage(response):
    return render(response, "main/eligiblePage.html", {})

def notEligiblePage(response):
    return render(response, "main/notEligiblePage.html", {})



