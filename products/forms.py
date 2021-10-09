from django import forms
from .widgets import CustomClearableFileUnit

from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('seller_store', 'has_sizes', 'rating', 'sku')

    image = forms.ImageField(label='Image', required=False, 
                             widget=CustomClearableFileUnit)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'price': 'Price per 250g',
            'name': 'Product Name',
            'description': 'Write a short description of your product...',
            'image_url': 'Image URL',
        }

        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field == 'price':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            if field == 'name':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            if field == 'description':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            if field == 'image_url':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        categories = Category.objects.all()
        friendly_names = [(c.category_id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
