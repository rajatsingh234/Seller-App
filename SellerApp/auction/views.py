from django.shortcuts import render
from .models import User, Auction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serlializers import AuctionSerializer


# Create your views here.
def create_auction(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        start_price = request.POST['start_price']
        user_id = User.objects.get(pk=id)
        auction = Auction.objects.create(
            item_name=item_name,
            start_time=start_time,
            end_time=end_time,
            start_price=start_price,
            user_id=user_id)
        auction.save()
        return render(request, "auction/home.html")
    return render(request, "auction/home.html")


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)


@api_view(['POST'])  # Create
def create_model(request):
    item_name = request.data['item_name']
    start_time = request.data['start_time']
    end_time = request.data['end_time']
    start_price = request.data['start_price']
    user_id = User.objects.get(pk=request.data['user_id'])
    auction = Auction.objects.create(
        item_name=item_name,
        start_time=start_time,
        end_time=end_time,
        start_price=start_price,
        user_id=user_id)

    # Return a response with the new item's details
    return Response({'item_name': auction.item_name, 'start_time': auction.start_time, 'end_time': auction.end_time,
                     'start_price': auction.start_price})


@api_view(['GET'])  # Read
def view_model(request):
    my_models = Auction.objects.all()
    serializer = AuctionSerializer(my_models, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])  # Delete
def delete_model(request, pk):
    my_model = Auction.objects.get(pk=pk)
    my_model.delete()
    return Response(status=204)


@api_view(['POST'])  # update
def update_model(request, pk):
    # Get the Auction object to be updated
    item = Auction.objects.get(id=pk)

    # Update the Auction object with the new data from the request
    item.item_name = request.data['item_name']
    item.start_time = request.data['start_time']
    item.end_time = request.data['end_time']
    item.start_price = request.data['start_price']
    item.save()

    # Return a response with the updated item's details
    return Response({'item_name': item.item_name, 'start_time': item.start_time, 'end_time': item.end_time,
                     'start_price': item.start_price})
