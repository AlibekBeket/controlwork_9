from django import forms

from gallery.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('signature', 'photo')

    def clean(self):
        cleaned_data = super().clean()
        signature = cleaned_data.get('signature')
        if len(signature) < 3:
            raise forms.ValidationError('Количество символов должно быть больше 2')
