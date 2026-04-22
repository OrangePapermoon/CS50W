from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    # any str inside <> would be passed to the greet function as a parameter
    path("hugh", views.hugh, name="hugh"),
    path("david", views.david, name="david")

]