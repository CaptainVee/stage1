from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Person
from .serializers import PersonSerializer

class PersonView(APIView):
    """
    Retrieve, post, update, or delete a Person instance.
    """

    def get_object(self, request):
        person_name = request.data.get('name')
        person_id = request.data.get('id')

        if person_id is not None:
            try:
                person = Person.objects.get(pk=person_id)
                return person
            except Person.DoesNotExist:
                raise Http404
        elif person_name is not None:
            try:
                person = Person.objects.get(name=person_name)
                return person
            except Person.DoesNotExist:
                raise Http404
        else:
            return None

    def get(self, request, format=None):
        person = self.get_object(request)
        if person is None:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        person = self.get_object(request)
        if person is None:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        person = self.get_object(request)
        if person is None:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
