from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'image']
        error_messages = {
            'title': {
                'required': 'Por favor, insira um título.',
                'max_length': 'O título não pode exceder 50 caracteres.',
            },
            'image': {
                'required': 'Por favor, selecione uma imagem para upload.',
            },
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        image = super().save(commit=False)
        if self.user:
            image.user = self.user
        if commit:
            image.save()
        return image
