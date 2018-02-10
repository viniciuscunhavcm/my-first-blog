from blog.models import *
from blog.serializers import *
from rest_framework import viewsets



class BlogView(viewsets.ModelViewSet):
	serializer_class = BlogSerializer;
	queryset = Equipamentos.objects.all();
	#serializer_class = BlogSerializer;


