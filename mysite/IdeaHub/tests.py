from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from IdeaHub.views import HomeView, IdeaDetailView, AddPostView, AddCategoryView, UpdatePostView, DeletePostView, CategoryView, LikeView, AddComment, UpdateCommentView,DeleteCommentView
from .models import Post, Category, Comment, Profile
from django.contrib.auth.models import User

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('IdeaHub:homepage')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_idea_detail_url_is_resolved(self):
        url = reverse('IdeaHub:idea_detail', args=[1])  # Assuming 1 is the id for a post
        self.assertEquals(resolve(url).func.view_class, IdeaDetailView)

    def test_add_post_url_is_resolved(self):
        url = reverse('IdeaHub:add_post')
        self.assertEquals(resolve(url).func.view_class, AddPostView)

    def test_update_post_url_is_resolved(self):
        url = reverse('IdeaHub:update_post', args=[1])  # Assuming 1 is the id for a post
        self.assertEquals(resolve(url).func.view_class, UpdatePostView)

    def test_delete_post_url_is_resolved(self):
        url = reverse('IdeaHub:delete_post', args=[1])  # Assuming 1 is the id for a post
        self.assertEquals(resolve(url).func.view_class, DeletePostView)

    def test_add_category_url_is_resolved(self):
        url = reverse('IdeaHub:add_category')
        self.assertEquals(resolve(url).func.view_class, AddCategoryView)

    def test_category_view_url_is_resolved(self):
        url = reverse('IdeaHub:category', args=['some-category'])
        self.assertEquals(resolve(url).func, CategoryView)

    def test_like_post_url_is_resolved(self):
        url = reverse('IdeaHub:like_post', args=[1])  # Assuming 1 is the id for a post
        self.assertEquals(resolve(url).func, LikeView)

    def test_add_comment_url_is_resolved(self):
        url = reverse('IdeaHub:add_comment', args=[1])
        self.assertEquals(resolve(url).func.view_class, AddComment)

    def test_update_comment_url_is_resolved(self):
        url = reverse('IdeaHub:update_comment', args=[1])  
        self.assertEquals(resolve(url).func.view_class, UpdateCommentView)

    def test_delete_comment_url_is_resolved(self):
        url = reverse('IdeaHub:delete_comment', args=[1])  
        self.assertEquals(resolve(url).func.view_class, DeleteCommentView)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('IdeaHub:homepage')
        self.user = User.objects.create_user('testuser', 'test@example.com', '12345') 
        self.profile = Profile.objects.create(user=self.user, bio='Test bio')
        self.category = Category.objects.create(name='test')
        self.post = Post.objects.create(
            title='Test Post',
            body='Test Body',
            author=self.user,
            category='test'
        )
        self.detail_url = reverse('IdeaHub:idea_detail', args=[self.post.id])
        self.add_post_url = reverse('IdeaHub:add_post')
        self.update_post_url = reverse('IdeaHub:update_post', args=[self.post.id])
        self.delete_post_url = reverse('IdeaHub:delete_post', args=[self.post.id])
        self.add_comment_url = reverse('IdeaHub:add_comment', args=[self.post.id])

    def test_HomeView_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_IdeaDetailView_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'idea_details.html')

    def test_AddPostView_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(self.add_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_AddCategoryView_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('IdeaHub:add_category'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_category.html')

    def test_UpdatePostView_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('IdeaHub:update_post', args=[self.post.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_post.html')

    def test_DeletePostView_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('IdeaHub:delete_post', args=[self.post.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_post.html')

    def test_CategoryView_GET(self):
        response = self.client.get(reverse('IdeaHub:category', args=[self.category.name]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_LikeView_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('IdeaHub:like_post', args=[self.post.id]), {'post_id': self.post.id}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())

    def test_AddComment_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('IdeaHub:add_comment', args=[self.post.id]), {
            'body': 'A new comment',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(body='A new comment', comment_author=self.user, post=self.post).exists())



    def test_UpdateCommentView_GET(self):
        self.client.force_login(self.user)
        comment = Comment.objects.create(post=self.post, comment_author=self.user, body='Original Comment')
        response = self.client.get(reverse('IdeaHub:update_comment', args=[comment.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_comment.html')

    def test_DeleteCommentView_GET(self):
        self.client.force_login(self.user)
        comment = Comment.objects.create(post=self.post, comment_author=self.user, body='Comment to be deleted')
        response = self.client.get(reverse('IdeaHub:delete_comment', args=[comment.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_comment.html')

    def tearDown(self):
        self.user.delete()
        self.post.delete()
        self.category.delete()

class Testmodels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.category1 = Category.objects.create(name='Test Category')
        self.post1 = Post.objects.create(
            title='Test Post',
            title_tag='Test Title Tag',
            author=self.user1,
            body='Body content here',
            category=self.category1.name
        )
        self.profile1 = Profile.objects.create(
            user=self.user1,
            bio='Bio here',
            website_url='http://example.com',
            facebook_url='http://facebook.com',
            instagram_url='http://instagram.com',
            github_url='http://github.com'
        )
        self.comment1 = Comment.objects.create(
            post=self.post1,
            comment_author=self.user1,
            body='Comment body here'
        )

    def test_post_model(self):
        self.assertEquals(self.post1.title, 'Test Post')
        self.assertEquals(self.post1.author, self.user1)
        self.assertEquals(self.post1.body, 'Body content here')
        self.assertEquals(self.post1.category, 'test category') 

    def test_category_model(self):
        self.assertEquals(self.category1.name, 'test category') 

    def test_profile_model(self):
        self.assertEquals(self.profile1.user, self.user1)
        self.assertEquals(self.profile1.bio, 'Bio here')
        self.assertEquals(self.profile1.website_url, 'http://example.com')

    def test_comment_model(self):
        self.assertEquals(self.comment1.post, self.post1)
        self.assertEquals(self.comment1.comment_author, self.user1)
        self.assertEquals(self.comment1.body, 'Comment body here')

    def test_post_total_likes(self):
        self.assertEquals(self.post1.total_likes(), 0) 

    def test_get_absolute_url_methods(self):
        self.assertEquals(self.post1.get_absolute_url(), '/')
        self.assertEquals(self.category1.get_absolute_url(), '/')
        self.assertEquals(self.profile1.get_absolute_url(), '/')
        self.assertEquals(self.comment1.get_absolute_url(), f'/ideja/{self.post1.pk}')