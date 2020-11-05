from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format = None):
        """Return a list of APIView Features"""
        an_apiview = [
           'Uses http methods as function (get, post, patch, put, delet)',
           'Is similar to a traditional django view',
           'Gives you the most control over your application logic',
           'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!' , 'an_apiview':an_apiview})
