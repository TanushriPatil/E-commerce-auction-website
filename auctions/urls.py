from django.urls import path

from . import views

#app_name = "auction"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addlisting", views.addlisting, name="addlisting"),
    path("category", views.category, name="category"),
    path("category/<str:cat_name>", views.categorylist, name="categorylist"),
    path("<int:item_id>/placebid", views.placebid, name="placebid"),
    path("<int:item_id>/soldOut", views.soldOutView, name="soldOutView"),
    path("soldouts", views.soldouts, name="soldouts"),
    path("<int:item_id>/watchlist", views.watchlist, name="watchlist" ),
    path("<int:item_id>/watchlistRemove", views.watchlistRemove, name="watchlistRemove" ),
    path("watchlist", views.watchlistView, name="watchlistView" ),

]
