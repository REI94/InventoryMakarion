from django.test import TestCase
from apps.producto.models import Producto

class ProductoTestCase(TestCase):
    def setUp(self):
        Producto.objects.create(
            codigo = 1421,
            nombre = "Bolso de cuero",
            categoria = "bolso",
            precio = 31000,
            precio_en_descuento = 26500,
            descripcion = "Con un acabado muy preciso, el bolso de cuero Makarión es sin duda uno de los mejor fabricados del sector.",
            cantidad = 4,
            disponible = True,
            unidades_vendidas = 7,                        
            texto_destacado = "Envíos gratis a todo el país.",
            caracteristica_destacada = "Fácil de lavar",
            caracteristica_destacada_2 = "Cuero real",
            caracteristica_destacada_3 = "Material muy resistente",
            caracteristica_destacada_4 = "Apropiado para cualquier ocasión",
            caracteristica_destacada_5 = "Cuero brillante"
        )

    def test_producto_labels(self):
        producto = Producto.objects.get(codigo=1421)        
        nombre_label = producto._meta.get_field('nombre').verbose_name
        descripcion_label = producto._meta.get_field('descripcion').verbose_name
        texto_destacado_label = producto._meta.get_field('texto_destacado').verbose_name
        caracteristica_destacada_label = producto._meta.get_field('caracteristica_destacada').verbose_name
        caracteristica_destacada_2_label = producto._meta.get_field('caracteristica_destacada_2').verbose_name
        caracteristica_destacada_3_label = producto._meta.get_field('caracteristica_destacada_3').verbose_name
        caracteristica_destacada_4_label = producto._meta.get_field('caracteristica_destacada_4').verbose_name
        caracteristica_destacada_5_label = producto._meta.get_field('caracteristica_destacada_5').verbose_name
        self.assertEqual(nombre_label, 'Nombre del producto')
        self.assertEqual(descripcion_label, 'Descripción')
        self.assertEqual(texto_destacado_label, 'Texto destacado')
        self.assertEqual(caracteristica_destacada_label, 'Característica destacada 1')
        self.assertEqual(caracteristica_destacada_2_label, 'Característica destacada 2')
        self.assertEqual(caracteristica_destacada_3_label, 'Característica destacada 3')
        self.assertEqual(caracteristica_destacada_4_label, 'Característica destacada 4')
        self.assertEqual(caracteristica_destacada_5_label, 'Característica destacada 5')
       
    def test_producto_length(self):
        producto = Producto.objects.get(codigo=1421)
        max_length_nombre = producto._meta.get_field('nombre').max_length
        max_length_texto_destacado = producto._meta.get_field('texto_destacado').max_length
        max_length_caracteristica_destacada = producto._meta.get_field('caracteristica_destacada').max_length
        max_length_caracteristica_destacada_2 = producto._meta.get_field('caracteristica_destacada_2').max_length
        max_length_caracteristica_destacada_3 = producto._meta.get_field('caracteristica_destacada_3').max_length
        max_length_caracteristica_destacada_4 = producto._meta.get_field('caracteristica_destacada_4').max_length
        max_length_caracteristica_destacada_5 = producto._meta.get_field('caracteristica_destacada_5').max_length
        self.assertEqual(max_length_nombre, 50)
        self.assertEqual(max_length_texto_destacado, 100)
        self.assertEqual(max_length_caracteristica_destacada, 60)
        self.assertEqual(max_length_caracteristica_destacada_2, 60)
        self.assertEqual(max_length_caracteristica_destacada_3, 60)
        self.assertEqual(max_length_caracteristica_destacada_4, 60)
        self.assertEqual(max_length_caracteristica_destacada_5, 60)

    def test_object_name_is_number_historia_plus_disease(self):
        producto = Producto.objects.get(codigo=1421)
        expected_object_name = '%s - %s'%(producto.codigo, producto.nombre)
        self.assertEqual(expected_object_name, str(producto))
    
    def test_get_absolute_url(self):
        producto = Producto.objects.get(codigo=1421)        
        self.assertEqual(producto.get_absolute_url(), '/producto/verProducto/1421')


