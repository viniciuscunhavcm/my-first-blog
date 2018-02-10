from rest_framework import serializers
from blog.models import *



class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Equipamentos
		fields = ('codigo_equipamento','marca_equipamento','modelo_equipamento','nome_equipamento','foto_equipamento')


		
