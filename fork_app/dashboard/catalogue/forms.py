from oscar.apps.dashboard.catalogue import forms as base_forms

class ProductForm(base_forms.ProductForm):

    class Meta(base_forms.ProductForm.Meta):

        fields = (
            'title', 'upc', 'video_url','is_featured', 'aliexpress_url', 'description', 'tutorial', 'is_discountable', 'structure')



