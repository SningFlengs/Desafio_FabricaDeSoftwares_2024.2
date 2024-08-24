from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError



class Image(models.Model):

    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        validators=[MinLengthValidator(1)],
        error_messages={
            'blank': 'O título não pode estar em branco.',
            'null': 'O título é obrigatório.',
            'min_length': 'O título deve ter pelo menos 1 caractere.',
        }
    )

    description = models.TextField(blank=True, null=True)

    image = CloudinaryField('image', blank=False, null=False, error_messages={
        'blank': 'Você deve enviar uma imagem.',
        'null': 'A imagem é obrigatória.'
    })

    image = CloudinaryField('image', blank=False, null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.description:
            return f"{self.title} - {self.description[:50]}"
        else:
            return self.title

    def clean(self):
        if "forbidden" in self.title:
            raise ValidationError("O título não pode conter a palavra 'forbidden'.")
