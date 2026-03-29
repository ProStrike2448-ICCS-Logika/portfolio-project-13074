from django.test import RequestFactory, TestCase

from auth_system.models import CustomUser

from .models import Post
from .views import PostListView


class PostListTest(TestCase):
    def test_heath_check(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_post_list_ajax(self):
        factory = RequestFactory()
        request = factory.get('/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = PostListView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PostModelTest(TestCase):
    def setUp(self):
        self.author = CustomUser.objects.create(
            username='test',
            password='test',
            phone_number='+000000000000',
            first_name='Test',
            last_name='Test',
        )

    def test_create_post(self):
        post = Post.objects.create(
            title='Test Post 1', content='Test Post 1 Content', author=self.author
        )
        self.assertEqual(post.title, 'Test Post 1')
        self.assertEqual(post.content, 'Test Post 1 Content')
        self.assertEqual(post.author, self.author)

    def test_str(self):
        post = Post.objects.create(
            title='Test Post 1', content='Test Post 1 Content', author=self.author
        )
        self.assertEqual(str(post), 'Test Post 1')

    def test_get_absolute_url(self):
        post = Post.objects.create(
            title='Test Post 1', content='Test Post 1 Content', author=self.author
        )
        self.assertEqual(post.get_absolute_url(), f'/{post.pk}/')
