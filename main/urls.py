from django.urls import path
from main import views

# <> (CAPTURE): Value Within <> In URL Path Will Be Passed Into A View Parameter.
urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("eligible/", views.eligiblePage, name="eligiblePage"),
    path("notEligible/", views.notEligiblePage, name="notEligiblePage"),
]
