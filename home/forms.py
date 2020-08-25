from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('start_date', 'end_date', 'course', 'school')

class TechSkillForm(forms.ModelForm):

    class Meta:
        model = TechSkill
        fields = ('skill',)

class OthersForm(forms.ModelForm):

    class Meta:
        model = Others
        fields = ('name', 'body')

class WorkExperienceForm(forms.ModelForm):

    class Meta:
        model = WorkExperience
        fields = ('start_date', 'end_date', 'role', 'where')

class PersonalInterestsForm(forms.ModelForm):

    class Meta:
        model = PersonalInterests
        fields = ('interest',)

class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = ('name', 'who', 'email', 'text')

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'link')

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('phone_number', 'address')