from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>", views.listing_page, name="listing_page"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("watchlist/<int:listing_id>/toggle", views.toggle_watchlist, name="toggle_watchlist"),
    path("listing/<int:listing_id>/bid", views.close_listing, name="close_listing"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category_name>/", views.category_listings, name="category_listings"),
]
