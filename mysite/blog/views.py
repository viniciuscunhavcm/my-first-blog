from django.shortcuts import render
from blog.models import *
from pyfcm import FCMNotification
from blog.serializers import BlogSerializer
from .forms import EquipamentosForm

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def inicio(request):
	return render(request, 'blog/index.html', {})

def listar(request):
	return render(request, 'blog/listar.html', {})



def apagar(request):

	if request.POST:

		eqp = Equipamentos.objects.get(codigo_equipamento=request.POST['codigo'])
		eqp.delete()

		return render(request, 'blog/index.html', {}) 
	else:	
		return render(request, 'blog/apagar.html', {})






def nuevo(request):

	#print(request.POST)

	if request.POST:
	
	
		print(request.POST)
		print(request.FILES)

		eqp = Equipamentos(codigo_equipamento=request.POST['codigo'], marca_equipamento = request.POST['marca'], modelo_equipamento = request.POST['modelo'],nome_equipamento = request.POST['nome'], foto_equipamento = request.FILES['foto'])
		eqp.save()


		#serializer = BlogSerializer(data=request.POST)
		#serializer = BlogSerializer(data=request)

		#if serializer.is_valid():
		#	serializer.save()

		#Enviar uma push notification a respeito da alteração do banco de dados:
		#push_service = FCMNotification(api_key="AAAAYCJjIj4:APA91bEjfaiaDoD-GIWiuiVWYo8EAmNPxrsKHuklpNk8TC_V-swOybV4cOmcIpxKm35tws3ZodpGObL0fRHl12vqWxUep_LQUms_nB2-XoBl8Tv0u-wzoTx_gsxbRVTr-BfOD8lvJABK")
		#registration_id = "foPpK50UUmY:APA91bFGJ9mdF8EvwEZJllKEQpKEFtzMlrOmDDYk6iTuNtAQn1frhx77aJ6x9fWCPSxxYCNR2XovEcV1OcakIHmh8nmp6XlPpCVtQkJlxqD2phlJvPGv8-Yxb6ju7fIixQreJkSJLdo3"
		#message_title = "Alerta Alteração Banco de Dados:"
		#message_body = "Novo equipamento salvo!"
		#result = push_service.notify_topic_subscribers(topic_name="news", message_body=message_body)
		#print(result)


		return render(request, 'blog/index.html', {}) 
	else:	
		return render(request, 'blog/nuevo.html', {})

    



def novo(request):

	
	if request.method =='POST':
	
		form = EquipamentosForm(request.POST, request.FILES)

		if form.is_valid():
			Codigo = form.cleaned_data['Codigo']
			Marca  = form.cleaned_data['Marca']
			Modelo = form.cleaned_data['Modelo']
			Nome   = form.cleaned_data['Nome']
			Foto   = form.cleaned_data['Foto']

			eqp = Equipamentos(Codigo,Marca,Modelo,Nome,Foto)
			eqp.save()

		else:
			print('A forma nao eh valida')			

		#print(request.POST)
		#eqp = Equipamentos(codigo_equipamento=request.POST['codigo'], marca_equipamento = request.POST['marca'], modelo_equipamento = request.POST['modelo'],nome_equipamento = request.POST['nome'], foto_equipamento = request.POST['foto'])
		#eqp.save()


		return render(request, 'blog/index.html', {}) 
	else:	
		return render(request, 'blog/novo.html', {})

