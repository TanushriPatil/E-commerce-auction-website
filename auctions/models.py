from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Listings(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    starting_bid = models.IntegerField()
    photo_url = models.CharField(max_length=600, blank=True)
    category = models.CharField(max_length=20)
    post_date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner", default=1)

    def __str__(self):
        return f"{self.id}"

class Bids(models.Model):

    item_id = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="ids")
    new_bid = models.IntegerField(default=1)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder", default=1)
    bid_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bids: {self.new_bid} by {self.username} for {self.item_id} on {self.bid_date}"

class Comments(models.Model):
    item_id = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="itemid")
    comment = models.CharField(max_length=700)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter", default="")

    def __str__(self):
        return f"{self.comment} - {self.username}"

class soldOut(models.Model):
    item_id = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ownerso", default=1)
    starting_bid = models.IntegerField()
    busername = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidderso", default=1)
    end_bid = models.IntegerField()
    post_date = models.DateTimeField()
    end_date = models.DateTimeField()
    photo_url = models.CharField(max_length=600, blank=True)
    title = models.CharField(max_length=100, default="None")
    category = models.CharField(max_length=20, default="None")

    def __str__(self):
        return f"This item was sold to {self.busername} on {self.end_date}"

class WatchList(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Watchlister", default=1)
    item_id = models.IntegerField()
    title = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=600, blank=True)
    category = models.CharField(max_length=20, default="None")
    starting_bid = models.IntegerField()

    def __str__(self):
        return f"{self.item_id} added to {self.username} watchlist"
