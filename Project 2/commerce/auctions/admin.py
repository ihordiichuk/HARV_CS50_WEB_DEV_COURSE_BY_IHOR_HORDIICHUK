from django.contrib import admin
from .models import Listing, Bid, User

# Register User model to appear in the Django admin panel
admin.site.register(User)

# Register Listing model so listings can be managed via admin interface
admin.site.register(Listing)

# Register Bid model to view and manage bids in admin
admin.site.register(Bid)