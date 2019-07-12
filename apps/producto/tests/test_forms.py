from django.test import TestCase
from apps.producto.forms import ProductoForm

class ProductoFormTest(TestCase):

    def test_form_fields_label(self):
        form = ProductoForm()
        self.assertTrue(form.fields['nombre'].label == 'Nombre')