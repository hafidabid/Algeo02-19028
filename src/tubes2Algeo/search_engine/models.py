from django.db import models

# Create your models here.

class filestorage(models.Model):
    url_dokumen =  models.CharField(max_length=100)
    url_sastrawee = models.CharField(max_length=100)
    judul = models.CharField(max_length=100)

    class Meta:
        db_table = "fileloc"