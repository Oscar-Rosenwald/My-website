from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User

import datetime

from home.models import Post
from home.models import Person
from home.models import Education
from home.models import WorkExperience
from home.models import TechSkill
from home.models import PersonalInterests
from home.models import Reference
from home.models import Project

from home.views import two_buttons
from home.views import cv_view
from home.views import blog_view

class CVTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("Me", "me@me.com", "memememe")
        self.person = Person()
        self.person.address = 'bla bla bla'
        self.person.me = self.user
        self.person.phone_number = '123'
        self.person.personal_others = ['thing', 'stuff', 'issues']
        self.person.save()

    def test_tech_skill_add_and_edit(self):
        tech = TechSkill()
        tech.skill = "Obtrusive smashing of strange people's windows with a heavy travel bag, mainly on Saturdays, and further running away from the viscous Labradors set lose on me by their rightful owners."
        tech.save()

        self.assertEqual(TechSkill.objects.count(), 1)

        tech2 = TechSkill()
        tech2.skill = "Leisurely assembly of metalic parts of old knitting machines which do not fit together; using living duct-tabe."
        
        tech.skill = "Exposing the polititians' lies with a ceramic hammer."

        tech.save()
        tech2.save()
        self.assertEqual(TechSkill.objects.count(), 2)
        self.assertIn("Exposing the polititians' lies with a ceramic hammer.", tech.skill)

    def test_personal_interests_add_and_edit(self):
        interest = PersonalInterests()
        interest.interest = "Two-headed, fire-breathing, scaly dolphins"
        interest.save()

        self.assertEqual(PersonalInterests.objects.count(), 1)

        interest2 = PersonalInterests()
        interest2.interest = "Adrenaline sleeping (don't try this at home)"
        
        interest.interest = "Zippa (It's like pizza, just inverted.)"

        interest.save()
        interest2.save()
        self.assertEqual(PersonalInterests.objects.count(), 2)
        self.assertIn("Zippa (It's like pizza, just inverted.)", interest.interest)

    def test_can_add_and_edit_projects(self):
        project = Project()
        project.name = "How to hack the FBI"
        project.description = "Self-evident"
        project.link = "http://www.staggeringbeauty.com"
        project.save()

        self.assertEqual(Project.objects.count(), 1)

    def test_can_add_and_edit_reference(self):
        ref1 = Reference()
        ref1.name = 'Nicolas Flamel'
        ref1.who = 'Mentor'
        ref1.email = 'flaming.flamel@immortal.org'
        ref1.text = "I have personally stood witness to this man's unspeakable talents. Unspeakable, as in it cannot be said just how much he lacks them. Truly, it is humanly impossible to underestimate this person."
        ref1.save()

        self.assertEqual(Reference.objects.count(), 1)

        ref2 = Reference()
        ref2.name = 'John Dee'
        ref2.who = 'Co-worker'
        ref2.email = 'Who-wants-the-Dee@gotohellnicolas.net'
        ref2.save()

        self.assertEqual(Reference.objects.count(), 2)

        ref2.text = "Don't listen to Nicolas, he's just jealous. I have the personal horour to present to you my eye vitnessness of just how great this applicant is. If you don't believe, do drop me an email."
        ref2.save()

        self.assertIn("he's just jealous", Reference.objects.get(name='John Dee').text)

    def test_can_save_and_edit_education(self):
        educ = Education()
        educ.start_date = datetime.datetime(1990, 2, 1, 1)
        educ.end_date = datetime.datetime(2020, 1, 2, 2)
        educ.course = 'Competitive cross-country-swimming'
        educ.school = "Xavier's School for Gifted Youngsters"
        educ.save()

        self.assertEqual(Education.objects.count(), 1)

        self.assertIn('Competitive cross-country-swimming', educ.course)
        self.assertIn("Xavier's School for Gifted Youngsters", educ.school)

        educ.course = 'Batman'
        educ.school = 'The Great and Wonderful University for Smart Kids, Illinois'
        educ.save()

        self.assertIn('Batman', educ.course)
        self.assertIn('The Great and Wonderful University for Smart Kids, Illinois',
                      educ.school)

    def test_can_save_an_address(self):
        self.assertEqual(Person.objects.count(), 1)

    def test_can_add_person_others(self):
        self.assertEqual(len(self.person.personal_others), 3)
        self.person.add_to_others(value='and others')
        self.assertEqual(len(self.person.personal_others), 4)

    def test_can_save_and_edit_work_experience(self):
        work_experience1 = WorkExperience()
        work_experience1.start_date = datetime.datetime(1913, 5, 11)
        work_experience1.end_date = datetime.datetime(2024, 11, 5)
        work_experience1.role = 'Bartender'
        work_experience1.where = 'Buckingham Palace'

        work_experience2 = WorkExperience()
        work_experience2.start_date = datetime.datetime(912, 12, 3)
        work_experience2.end_date = datetime.datetime(3000, 1, 31)
        work_experience2.role = 'Screenwriter'
        work_experience2.where = "The Queen's Biography, BBC"

        work_experience1.save()
        work_experience2.save()

        self.assertEqual(WorkExperience.objects.count(), 2)

        self.assertIn('Screenwriter', work_experience2.role)
        work_experience2.role = 'Professional nudist'
        work_experience2.save()
        self.assertIn('Professional nudist', work_experience2.role)

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, two_buttons)

    def test_CV_url_resolves_correctly(self):
        found = resolve('/cv')
        self.assertEqual(found.func, cv_view)

    def test_blog_url_resolves_correctly(self):
        found = resolve('/blog')
        self.assertEqual(found.func, blog_view)

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_has_correct_title(self):
        response = self.client.post('/')
        self.assertIn('<h2>My School CV thingy</h2>', response.content.decode())

    def test_home_has_two_buttons(self):
        response = self.client.post('/')

        self.assertIn('button', response.content.decode())

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("Me", "me@me.com", "memememe")

    def test_database_has_posts(self):
        post = Post()
        post.title = "Ahoy"
        post.text = "AaaaaaHooooYYYYY"
        post.author = self.user
        post.save()
        self.assertEqual(Post.objects.count(), 1)