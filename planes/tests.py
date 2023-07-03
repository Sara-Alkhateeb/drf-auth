from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Plane


# Create your tests here.

class PlaneTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser.save()

        test_Plane = Plane.objects.create(name='Boeing 747-8', owner=testuser, desc="test desc ...")
        test_Plane.save()

    def planes_model(self):
        Plane = Plane.objects.get(id=1)
        actual_owner= str(Plane.owner)
        actual_name = str(Plane.name)
        actual_desc = str(Plane.desc)
        self.assertEqual(actual_owner,"testuser")
        self.assertEqual(actual_name,"Boeing 747-8")
        self.assertEqual(actual_desc,"test desc ...")

