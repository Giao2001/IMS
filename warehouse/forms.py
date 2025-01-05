from crispy_forms.helper import FormHelper
from django import forms
from warehouse.models import Warehouse


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['wh_code', 'wh_name', 'wh_comment', 'wh_bg']

        widgets = {
            'wh_comment': forms.Textarea(),
        }

        labels = {
            'wh_bg': 'Background Image'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False





