from django.forms import ModelForm
from core.erp.models import Category


class categoryForm(ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


