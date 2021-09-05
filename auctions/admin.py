from django.contrib import admin
from .models import *

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ("username", "email")

class listingAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "starting_bid", "photo_url", "category", "post_date" , "username")

class bidsAdmin(admin.ModelAdmin):
    list_display = ("item_id", "new_bid", "username", "bid_date")

class commentAdmin(admin.ModelAdmin):
    list_display = ("item_id", "comment", "username")

class soldOutAdmin(admin.ModelAdmin):
    list_display = ("item_id", "username", "starting_bid", "busername", "end_bid", "post_date", "end_date")

class watchlistAdmin(admin.ModelAdmin):
    list_display = ("username", "item_id", "title", "photo_url", "category", "starting_bid")



admin.site.register(User, userAdmin)
admin.site.register(Listings, listingAdmin)
admin.site.register(Bids, bidsAdmin)
admin.site.register(Comments, commentAdmin)
admin.site.register(soldOut, soldOutAdmin)
admin.site.register(WatchList, watchlistAdmin)
