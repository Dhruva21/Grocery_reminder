from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Grocery
from .serializers import GrocerySerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/groceries/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of groceries'
        },
        {
            'Endpoint': '/groceries/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single grocery item'
        },
        {
            'Endpoint': '/groceries/add/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new grocery item with data sent in post request'
        },
        {
            'Endpoint': '/groceries/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing grocery with data sent in post request'
        },
        {
            'Endpoint': '/groceries/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting grocery'
        },
    ]
    return Response(routes)

# get the groceries end point
@api_view(['GET'])
def getGroceries(request):
    groceries = Grocery.objects.all() # for getting all the groceries
    serializer = GrocerySerializer(groceries, many=True)
    return Response(serializer.data)

# add the grocery to the table
@api_view(['POST'])
def addGrocery(request):
    data = request.data
    grocery = Grocery.objects.create(
        body=data['body']
    )
    serializer = GrocerySerializer(grocery, many=False)
    return Response(serializer.data)

# '/grocery/id'
# get the grocery item based on the id
@api_view(['GET'])
def getGrocery(request, pk):
    grocery = Grocery.objects.get(id=pk)
    serializer = GrocerySerializer(grocery, many=False)
    return Response(serializer.data)

# /grocery/id/update/
@api_view(['PUT'])
def updateGrocery(request, pk):
    data = request.data
    grocery = Grocery.objects.get(id=pk)
    serializer = GrocerySerializer(instance=grocery, data=data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# /grocery/id/delete/
@api_view(['DELETE'])
def deleteGrocery(request, pk):
    grocery = Grocery.objects.get(id=pk)
    # use delete method to get rid of the grocery item completely from the database
    grocery.delete()
    return Response('Grocery Item was deleted.')
