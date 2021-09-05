from django.test import TestCase
from polls.models import User, Status_data, Directory, File ,File_section, Section_category, Section_status, FramaOutput, Status_data

import datetime

# pages/tests.py
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from django.utils import timezone

from . import views

class FramaOutputTestCase(TestCase):
    def setUp(self):
        lion = FramaOutput()
        lion.phrase = "lion"
        lion.output = "roar"
        lion.save()

    def test_frama(self):
        lion = FramaOutput.objects.get(phrase="lion")
        self.assertTrue(lion.outputt()=="roar")
        
class UserTestCase(TestCase):
    def setUp(self):
        lion = User()
        lion.login = "lion123"
        lion.password = "roar"
        lion.name = "lion"
        lion.pub_date = datetime.datetime.now()
        lion.validity_flag = True
        lion.save()

    def test_user(self):
        lion = User.objects.get(login="lion123")
        self.assertTrue(lion.passw()=="roar")
        
        
class FileTestCase(TestCase):
    def setUp(self):
        post = File()
        post.directory_name = "directory_name"
        post.optional_description = "optional_description"
        post.creation_date = datetime.datetime.now()
        post.owner = "owner"
        post.filepath = "full_file"
        post.name = "files"
        post.validity_flag = True
        post.save()

    def test_file(self):
        lion = File.objects.get(directory_name="directory_name")
        self.assertTrue(lion.ret_owner()=="owner")
        
        
        
class DirectoryTestCase(TestCase):
    def setUp(self):
        post = Directory()
        post.name = "directory_name"
        post.optional_description = "optional_description"
        post.owner = "owner"
        post.creation_date = datetime.datetime.now()
        post.validity_flag = True
        dirname = post.name
        post.save()

    def test_directory(self):
        lion = Directory.objects.get(name="directory_name")
        self.assertTrue(lion.owner=="owner")
                

class StatusDataTestCase(TestCase):
    def setUp(self):
        lion = User()
        lion.login = "lion123"
        lion.password = "roar"
        lion.name = "lion"
        lion.pub_date = datetime.datetime.now()
        lion.validity_flag = True
        lion.save()
        lion = Status_data()
        lion.status_data_field = "lion"
        lion.user = User.objects.get(login="lion123")
        lion.save()

    def test_status_data(self):
        lion = Status_data.objects.get(status_data_field="lion")
        cos = User.objects.get(login="lion123")
        self.assertTrue(lion.user==cos)
        
        

class SectionStatusaTestCase(TestCase):
    def setUp(self):
        lion = User()
        lion.login = "lion123"
        lion.password = "roar"
        lion.name = "lion"
        lion.pub_date = datetime.datetime.now()
        lion.validity_flag = True
        lion.save()
        lion = Section_status()
        lion.status_data_field = "lion"
        lion.user = User.objects.get(login="lion123")
        lion.pub_date = datetime.datetime.now()
        lion.validity_flag = True
        lion.save()

    def test_section_status(self):
        lion = Section_status.objects.get(status_data_field="lion")
        cos = User.objects.get(login="lion123")
        self.assertTrue(lion.user==cos)
        
class FileSectionTestCase(TestCase):
    def setUp(self):
        post = File_section()
        post.name = "costam"
        post.optional_description = "bleeeeeeeeeeeeeeeeeeeeeeeeeee"
        post.creation_date = datetime.datetime.now()
        post.owner = "lion123"
        post.validity_flag = True
        post.file = "exfile"
        post.save()

    def test_file_section(self):
        lion = File_section.objects.get(name="costam")
        self.assertTrue(lion.file=="exfile")
    
def create_files_list():
        post = File()
        post.directory_name = "directory_name"
        post.optional_description = "optional_description"
        post.creation_date = datetime.datetime.now()
        post.owner = False
        post.filepath = "full_file"
        post.name = "files"
        post.validity_flag = True
        post.save()
        return post
        
def create_directory_list():
        post = Directory()
        post.name = "directory_name"
        post.optional_description = "optional_description"
        post.owner = False
        post.creation_date = datetime.datetime.now()
        post.validity_flag = True
        post.save()
        return post


class IndexViewTests(TestCase):
    def test_index(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        
class LoginViewTests(TestCase):
    def test_login(self):
        response = self.client.get(reverse('polls:login'))
        self.assertEqual(response.status_code, 200)
        
class LoginViewTests(TestCase):
    def test_login(self):
        response = self.client.get(reverse('polls:logout'))
        self.assertEqual(response.status_code, 302)
        
class LoginTerminateViewTests(TestCase):
    def test_login(self):
        response = self.client.get(reverse('polls:login_terminate'))
        self.assertEqual(response.status_code, 200)
        
class AddFileViewTests(TestCase):
    def test_af(self):
        response = self.client.get(reverse('polls:add_file'))
        self.assertEqual(response.status_code, 200)
      
class AddFileAccViewTests(TestCase):
    def test_afacc(self):
        response = self.client.get(reverse('polls:add_file_acc'))
        self.assertEqual(response.status_code, 200)
        
class AddDirectoryViewTests(TestCase):
    def test_af(self):
        response = self.client.get(reverse('polls:add_directory'))
        self.assertEqual(response.status_code, 200)
      
class AddDirectoryAccViewTests(TestCase):
    def test_afacc(self):
        response = self.client.get(reverse('polls:add_directory_acc'))
        self.assertEqual(response.status_code, 200)
        
class DeleteFileViewTests(TestCase):
    def test_df(self):
        response = self.client.get(reverse('polls:delete_file'))
        self.assertEqual(response.status_code, 200)

class DetailViewTests(TestCase):
    def test_detail(self):
        directory_sth = create_directory_list()
        sth = create_files_list()
        url = reverse('polls:detail', args=(directory_sth.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class DeleteFileNumberViewTests(TestCase):
    def test_delete_file_number(self):
        directory_sth = create_directory_list()
        sth = create_files_list()
        url = reverse('polls:delete_file_number', args=(sth.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        

        
#testy na formsy!!

class FormsBasicTests(TestCase):
    def test_index(self):
        url = reverse('polls:index')
        response = self.client.post(url, {'login' : 'manus1235'})
        self.assertEqual(response.status_code, 200)
        
class AddFileAccFormTests(TestCase):
    def test_afacc(self):
        url = reverse('polls:add_file_acc')
        response = self.client.post(url, {'directory_name': 'dir_name', 'owner': 'owner', 'full_file': 'sth_file'})
        self.assertEqual(response.status_code, 200)
        
        
class AddDirectoryAccFormTests(TestCase):
    def test_afacc(self):
        url = reverse('polls:add_directory_acc')
        response = self.client.post(url, {'directory_name': 'dir_name', 'owner': 'owner', 'optional_description': 'sth'})
        self.assertEqual(response.status_code, 200)       
        
        

  