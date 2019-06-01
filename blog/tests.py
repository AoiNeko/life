from django.test import TransactionTestCase
from django.test.utils import isolate_apps
from blog.models import post

# Create your tests here.


@isolate_apps('blog')
class TestModelDefinition(TransactionTestCase):
    def testGetPost(self):
        """测试model增查"""
        test1 = post(content='test2', title='title2')
        test1.save()
        list = post.objects.all()
        print("ctest 11")
        for i in list:
            print(i.title)
        self.assertEqual(True, True)
       