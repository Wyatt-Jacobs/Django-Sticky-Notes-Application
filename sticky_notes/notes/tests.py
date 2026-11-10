from django.test import TestCase
from django.urls import reverse
from .models import Note, Author

# Create your tests here.
class NoteModelTest(TestCase):
    def setUp(self):
        # Create Author object
        author = Author.objects.create(name='Test Author') 
        # Create Note object
        note = Note.objects.create(title='Test note', 
                                   content='This is a test note.', 
                                   author=author)  
        
    def test_note_has_title(self):
        # Test that note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test note')
        
    def test_note_has_content(self):
        # Test that note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')
        
class PostViewTest(TestCase):
    def setUp(self):
            # Create Author object
            author = Author.objects.create(name='Test Author') 
            # Create Note object
            note = Note.objects.create(title='Test note', 
                                       content='This is a test note.', 
                                       author=author)  
            
    def test_note_list(self):
        # Test the note-list view
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test note')
        
    def test_note_detail_view(self):
        # Test the note-detail view
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_detail', args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test note')
        self.assertContains(response, 'This is a test note.')        