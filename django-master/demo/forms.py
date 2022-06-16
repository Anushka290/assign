from django.forms import ModelForm
from .models import book


class bookform(ModelForm):
	class Meta:
		model = book
		fields = '__all__'