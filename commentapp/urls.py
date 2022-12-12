from django.urls import path
from commentapp import views

urlpatterns=[
path("post_detail/",  views.post_detail, name="post_detail"),

# path('<slug:slug/',, name='post_detail'),
]
