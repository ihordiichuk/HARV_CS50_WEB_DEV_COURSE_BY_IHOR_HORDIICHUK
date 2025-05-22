from django.urls import path
from . import views

# Define all URL routes for the auctions app
urlpatterns = [
    # Homepage - shows all active listings
    path("", views.index, name="index"),

    # Authentication routes
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # Route to create a new auction listing
    path("create", views.create_listing, name="create_listing"),

    # View a specific listing by its ID
    path("listing/<int:listing_id>", views.listing_page, name="listing_page"),

    # Close an active listing (owner only)
    path("listing/<int:listing_id>/close", views.close_listing, name="close_listing"),

    # Toggle watchlist status for a listing
    path("listing/<int:listing_id>/toggle", views.toggle_watchlist, name="toggle_watchlist"),

    # View user's watchlist
    path("watchlist", views.watchlist_view, name="watchlist"),

    # View all categories
    path("categories", views.categories, name="categories"),

    # View listings by specific category name
    path("categories/<str:category_name>", views.category_listings, name="category_listings"),
]