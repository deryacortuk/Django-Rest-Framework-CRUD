from django.urls import path
from .views import FollowerListView,FollowerDetailView

app_name='follower'

urlpatterns = [
    path('', FollowerListView.as_view(),name="follower_list"),
    path('<int:id>',FollowerDetailView.as_view(),name='follower'),
   
]
