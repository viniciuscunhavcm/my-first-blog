from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Equipamentos(models.Model):
	codigo_equipamento = models.CharField(max_length=200)
	marca_equipamento  = models.CharField(max_length=200)
	modelo_equipamento = models.CharField(max_length=200)
	nome_equipamento   = models.CharField(max_length=200)
	foto_equipamento   = models.FileField(upload_to='', null=True, blank=True)

	def __unicode__(self):
		return "%s" %(self.nome_equipamento)