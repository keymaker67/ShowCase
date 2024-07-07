from unittest import skip

from django.test import TestCase

from django.contrib.auth import get_user_model
from store.models import CategoryModel, ProductModel
from django.urls import reverse

from django.test import Client

the_user = get_user_model()


# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.client = Client()

    # CategoryModel.objects.create(name='django1', slug='django')
    # the_user.objects.create(username='admin')
    # self.data1 = ProductModel.objects.create(
    #     category_id=1,
    #     created_by_id=1,
    #     price='99.99',
    #     image='django',
    #     title='django beginners',
    #     slug='the_django-beginners'
    # )

    def test_homepage_url(self):
        """
        Test homepage response
        """
        response = self.client.get('/store/')
        self.assertEqual(response.status_code, 200)

    # def test_product_detail_url(self):
    #     response = self.client.get(reverse('store:product_detail', args=['the_django-beginners']))
    #     self.assertEqual(response.status_code, 200)
