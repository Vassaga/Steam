from django.urls import path

# Local
from .views import GameView, MainView, GameListView, about


urlpatterns = [
    path('', MainView.as_view()),
    path('about/', about),
    path('list/<int:game_id>/', GameView.as_view()),
    path('list/', GameListView.as_view()),
]
