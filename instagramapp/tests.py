from django.test import TestCase


# Create your tests here.
from .models import Image
from django.core.files.uploadedfile import SimpleUploadedFile


class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):


        self.test_image = Image.objects.create(image='imagesef',
                                name='cat',
                                description='This is a description',

                                )

        self.test_image.save()

    def test_save_method(self):
        self.test_image.save()
        test_images = Image.objects.all()
        self.assertTrue(len(test_images) > 0)

    # Testing save method
    def test_save_image(self):
        self.assertEqual(len(Image.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Image.objects.all().delete()

    def test_delete_image(self):
        Image.delete_image_by_id(self.test_image.id)
        self.assertEqual(len(Image.objects.all()), 0)


