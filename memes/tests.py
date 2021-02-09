from django.test import TestCase
from .models import Meme


class MemeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Meme.objects.create(name='first meme')
        Meme.objects.create(url='a url here')
        Meme.objects.create(caption='a caption here')

    def test_name_content(self):
        meme = Meme.objects.get(id=1)
        expected_object_name = f'{meme.name}'
        self.assertEquals(expected_object_name, 'first meme')

    def test_url_content(self):
        meme = Meme.objects.get(id=2)
        expected_object_name = f'{meme.url}'
        self.assertEquals(expected_object_name, 'a url here')

    def test_caption_content(self):
        meme = Meme.objects.get(id=3)
        expected_object_name = f'{meme.caption}'
        self.assertEquals(expected_object_name, 'a caption here')