from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    is_active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, related_name='watchlist', blank=True)
    
    def current_price(self):
        highest = self.bids.order_by("-amount").first()
        return highest.amount if highest else self.starting_bid

    def winner(self):
        highest = self.bids.order_by('-amount').first()
        return highest.user if highest else None
    
    def __str__(self):
        return f"{self.title} | Starting Bid: ${self.starting_bid}"
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_as_owner")
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_as_bidder")





