from django.test import TestCase
from django.contrib.auth import get_user_model

from store.models import CategoryModel, ProductModel

User = get_user_model()


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = CategoryModel.objects.create(name='django', slug='django')

    def test_category_model_entry_1(self):
        """
        Test Category model data insertion/types/fields attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, CategoryModel))
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self):
        CategoryModel.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = ProductModel.objects.create(
            category_id=1,
            created_by_id=1,
            price='99.99',
            image='django',
            title='django beginners',
            slug='django-beginners'
        )

    def test_category_model_entry_1(self):
        """
        Test Category model data insertion/types/fields attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, ProductModel))
        self.assertEqual(str(data), 'django beginners')
        data = self.data1
