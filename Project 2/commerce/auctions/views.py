from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ListingForm
from .models import Bid, Listing, User


def index(request):
    # Show all listings on the homepage
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":
        # Authenticate user with submitted credentials
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })

    return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


def register(request):
    if request.method == "POST":
        # Gather registration info
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return redirect("index")

    return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect("index")
    else:
        form = ListingForm()

    return render(request, "auctions/create_listing.html", {
        "form": form
    })


@login_required
def close_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    # Only owner can close their own listing
    if request.user != listing.owner:
        return HttpResponseForbidden("Only the owner can close the listing.")

    listing.is_active = False
    listing.save()
    return redirect("listing_page", listing_id=listing.id)


def listing_page(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    bids = listing.bids.order_by("-timestamp")
    is_owner = request.user == listing.owner if request.user.is_authenticated else False
    highest_bid = listing.bids.order_by("-amount").first()

    if request.method == "POST":
        if not listing.is_active:
            messages.error(request, "This auction is closed.")
            return redirect("listing_page", listing_id=listing.id)

        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to place a bid.")
            return redirect("login")

        try:
            new_bid = float(request.POST["bid"])
        except ValueError:
            messages.error(request, "Invalid bid format.")
        else:
            current_price = highest_bid.amount if highest_bid else listing.starting_bid
            if new_bid > current_price:
                Bid.objects.create(user=request.user, listing=listing, amount=new_bid)
                messages.success(request, "Your bid was placed successfully.")
                return redirect("listing_page", listing_id=listing.id)
            else:
                messages.error(request, "Your bid must be higher than the current price.")

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bids": bids,
        "highest_bid": highest_bid,
        "is_owner": is_owner
    })


@login_required
def toggle_watchlist(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    # Add/remove listing from watchlist depending on current state
    if request.user in listing.watchlist.all():
        listing.watchlist.remove(request.user)
    else:
        listing.watchlist.add(request.user)

    return redirect("listing_page", listing_id=listing.id)


@login_required
def watchlist_view(request):
    # Show all listings the user has added to their watchlist
    listings = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })


def categories(request):
    # Show list of available categories
    categories = Listing.CATEGORY_CHOICES
    return render(request, "auctions/categories.html", {
        "categories": categories
    })


def category_listings(request, category_name):
    # Show all active listings within a given category
    listings = Listing.objects.filter(category=category_name, is_active=True)
    return render(request, "auctions/category_listings.html", {
        "listings": listings,
        "category_name": category_name
    })