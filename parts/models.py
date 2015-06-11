from django.db import models

# Create your models here.


class Part(models.Model):
    sprezyna = 'sp'
    sruba = 'sr'
    lozysko = 'lo'

    PART_TYPE_CHOICES =(
        (sprezyna,'sprezyna'),
        (sruba,'sruba'),
        (lozysko,'lozysko'),
    )
    name = models.CharField('Nazwa czesci', max_length=100)
    id_name =  models.CharField('Numer czesci', max_length=100)
    parttype = models.CharField('Typ czesci', max_length=10, choices=PART_TYPE_CHOICES, default=sruba)
    pic = models.ImageField(upload_to='images/')
    def __str__(self):
        return "{nazwa} {id_name} {parttype}".format(
            nazwa=self.name,
            id_name = self.id_name,
            parttype = self.get_parttype_display(),# get_NAZWAPOLA_display
            )


