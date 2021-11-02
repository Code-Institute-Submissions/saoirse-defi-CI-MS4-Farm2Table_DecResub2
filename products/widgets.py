from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class ProductClearableFileUnit(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = ('products/custom_widget_templates/',
                     'product_clearable_file_unit.html')
