from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "auctions/index.html", {
        "items": Listings.objects.all().order_by('-post_date')
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = name;
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def addlisting(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST.get("starting_bid")
        photo_url = request.POST["photo_url"]
        category = request.POST["category"]

        items = Listings(
            title= title.capitalize(),
            description= description.capitalize(),
            starting_bid= starting_bid,
            photo_url= photo_url,
            category= category,
            post_date= timezone.now(),
            username=request.user
        )
        items.save()

        return render(request, "auctions/index.html" , {
            "items": Listings.objects.all().order_by('-post_date')
        })
    else:
        return render(request, "auctions/addlisting.html")

def category(request):
    return render(request, "auctions/category.html", {
    "cats":("Clothing", "Electronics", "Toys", "Furniture", "Music", "Books")
    })

def categorylist(request, cat_name):

    list = Listings.objects.filter(category=cat_name).order_by('-post_date')

    return render(request, "auctions/index.html" , {
        "items": list
    })


def placebid(request, item_id):
    if request.method == "POST":
        bid = request.POST.get("mybid");
        comment = request.POST.get("comment");
        l1 = Listings.objects.get(id=item_id)
        u1 = User.objects.get(username=request.user)
        msg2 = None
        msg = None

        if comment:
            test_comment = Comments.objects.all().filter(item_id=item_id, username=request.user)
            if test_comment:
                msg2 = "You've already commented. Cannot put another comment."
            else:
                c1 = Comments(
                        item_id=l1,
                        comment=comment,
                        username=u1
                    )
                c1.save()
                msg2 = "Comment posted!"
        if bid:
            check_bidder = Bids.objects.all().filter(item_id=item_id, username=request.user)
            if not check_bidder:
                test_bid = Bids.objects.all().filter(item_id=item_id)
                if not test_bid:
                    data = l1.starting_bid
                else:
                    data = test_bid.order_by('-bid_date')[0].new_bid


                if int(bid) > data:
                    b1 = Bids(item_id=l1, new_bid=bid, username=u1, bid_date=timezone.now())
                    b1.save()
                    msg = "Bid placed"
                else:
                    msg = "Error: Enter bid greater than original price and the last bid price! "
            else:
                msg = "Cannot bid more than once!"

        item = Listings.objects.get(id=item_id)
        obj = WatchList.objects.all().filter(item_id=item_id, username=u1)
        if obj:
            msg4="In your watchlist"
        else:
            msg4=None
        if not item:
            item = soldOut.objects.get(item_id=item_id)
            return render(request, "auctions/placebid.html", {
                "item": item,
                "msg3":"This item is sold out!",
                "soldtoname": item.busername,
                "soldat": item.end_bid,
                "msg4": msg4,
                "msg": msg,
                "msg2":msg2,
                "count": Bids.objects.all().filter(item_id=item_id).count()
            })
        else:
            return render(request, "auctions/placebid.html", {
                "item": item,
                "bids": Bids.objects.all().filter(item_id=item_id).order_by('-bid_date'),
                "comments": Comments.objects.all().filter(item_id=item_id),
                "msg4": msg4,
                "msg": msg,
                "msg2":msg2,
                "count": Bids.objects.all().filter(item_id=item_id).count()
            })


    else:

        u1 = User.objects.get(username=request.user)
        print(item_id)
        item = Listings.objects.get(id=item_id)
        obj = WatchList.objects.all().filter(item_id=item_id, username=u1)
        if obj:
            msg4="In your watchlist"
        else:
            msg4=None
        if not item:
            item = soldOut.objects.get(item_id=item_id)
            return render(request, "auctions/placebid.html", {
                "item": item,
                "msg3":"This item is sold out!",
                "soldtoname": item.busername,
                "soldat": item.end_bid,
                "msg4": msg4
            })
        else:
            return render(request, "auctions/placebid.html", {
                "item": item,
                "bids": Bids.objects.all().filter(item_id=item_id).order_by('-bid_date'),
                "comments": Comments.objects.all().filter(item_id=item_id),
                "msg4": msg4
            })


def soldOutView(request, item_id):
    if request.method == "POST":

        #Get the owner of the item
        l1 = Listings.objects.get(id=item_id)
        u1 = User.objects.get(username = l1.username)
        #Get the highest bidder for that item
        b1 = Bids.objects.all().filter(item_id=item_id).order_by('-bid_date')[0]
        u2 = User.objects.get(username=b1.username)
        item = Listings.objects.get(pk=item_id)
        #Get starting prce, last bid, starting Date, end date
        start_price = l1.starting_bid
        end_price = b1.new_bid
        starting_date = l1.post_date
        ending_date = b1.bid_date
        pic_url = l1.photo_url
        title = l1.title
        category = l1.category

        s = soldOut(
                item_id=item_id,
                username=u1,
                starting_bid=start_price,
                busername=u2,
                end_bid=end_price,
                post_date=starting_date,
                end_date=ending_date,
                photo_url = pic_url,
                title = title,
                category=category
            )
        s.save()
        #Delete entry from listings as it's no longer active
        l1.delete()

        return render(request, "auctions/placebid.html", {
            "item": item,
            "msg3":"This item is sold out!",
            "soldtoname": s.busername,
            "soldat": s.end_bid
        })

def soldouts(request):
    return render(request, "auctions/soldouts.html", {
        "items":soldOut.objects.all().order_by('-end_date')
    })


@login_required
def watchlist(request, item_id):
    if request.method == "POST":
        # Get the user who posted the listing
    #    add = request.POST['add']
        obj = Listings.objects.get(pk=item_id)
        u1 = User.objects.get(username=request.user)
        watch = WatchList(
            username=u1,
            item_id=item_id,
            title=obj.title,
            photo_url=obj.photo_url,
            category=obj.category,
            starting_bid=obj.starting_bid
        )
        watch.save()

        item = Listings.objects.get(pk=item_id)
        if not item:
            item = soldOut.objects.get(item_id=item_id)

        return render(request, "auctions/placebid.html", {
            "item": item,
            "bids": Bids.objects.all().filter(item_id=item_id).order_by('-bid_date'),
            "comments": Comments.objects.all().filter(item_id=item_id),
            "msg4": "Item added to wishlist"
        })

def watchlistRemove(request, item_id):
    if request.method == "POST":
        u1 = User.objects.get(username=request.user)
        watch = WatchList.objects.all().filter(username=u1, item_id=item_id)
        watch.delete()

        return render(request, "auctions/watchlist.html", {
            "items": WatchList.objects.all().filter(username=u1)
        })



def watchlistView(request):
    u1 = User.objects.get(username=request.user)
    msg4 = "In your watchlist"

    return render(request, "auctions/watchlist.html", {
        "items": WatchList.objects.all().filter(username=u1)

    })
