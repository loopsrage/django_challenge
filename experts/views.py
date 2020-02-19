from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from . import serializers
from . import models

# Create your views here.


class ExpertViewSet(ModelViewSet):
    """Viewset for CRUD functionality of Expert objects"""
    serializer_class = serializers.ExpertSerializer
    queryset = models.Experts.objects.all()

    @action(detail=False, methods=['post', ])
    def add_friend(self, request, pk=None):
        """Api call to send a friend request"""
        pass

    @action(detail=True, methods=['post', ])
    def search_friends(self, request, pk=None):
        """Api call to return friend results based on search input
        the user you are viewing acts as a starting point for a tree.

        1. Enter the search term
        2. Search the current users friends
        3. For each of the results, look for search term in content
        4. If search term is there, save the user as a second connection
        5. Recursively search up to 10 levels of friends

        Results output as:
        """
        search_term = request.data['search']
        selected_user = get_object_or_404(models.Experts, pk=pk)

        selected_user.friends.all()

        return Response("response")
