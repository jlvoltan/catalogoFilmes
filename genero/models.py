from django.db import models

class GeneroFormulario(models.Model):
    descricao = models.CharField(max_length=58)
    def __str__(self): return self.descricao
    def getDescricao(self):return self.descricao

