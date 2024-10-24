from django.db import models

class Topic(models.Model):
    """ Um Assunto Direto """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        """ Devolve a string do modelo """
        return self.text
    
