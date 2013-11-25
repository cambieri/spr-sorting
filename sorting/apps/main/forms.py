# coding: utf-8
from django import forms

class UploadForm(forms.Form):
    ima_file = forms.FileField(
        label='Seleziona il file IMA',
        help_text='Dimensione massima: 12 Mbytes'
    )
