from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User

from home.forms import *

from home.models import Post
from home.models import Person
from home.models import Education
from home.models import TechSkill
from home.models import WorkExperience
from home.models import PersonalInterests
from home.models import Reference
from home.models import Others

def two_buttons(request):
    return render(request, 'home.html')

def cv_view(request):
    # Personal Details
    me = User.objects.get(username='Cyril-Saroch')
    person = Person.objects.get(me=me)
    name = person.me.first_name + " " + person.me.last_name
    email = person.me.email
    phone_number = person.phone_number
    address = person.address

    others = Others.objects.filter(person=person)

    # Education
    education = Education.objects.order_by('-end_date')

    # Tech skills
    tech = TechSkill.objects.all()

    # Work experience
    exp = WorkExperience.objects.order_by('-end_date')

    # Personal Interests
    interests = PersonalInterests.objects.all()

    # References
    refs = Reference.objects.all()

    # Projects
    projects = Project.objects.all()

    return render(request, 'CVs.html', {'projects': projects, 'personal_others': others, 'tech_skills': tech, 'personal_interests': interests, 'references': refs, 'name': name, 'email': email, 'address': address, 'phone_number': phone_number, 'education': education, 'work_experience': exp})

def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})

def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('posts', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('posts', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})

def education_new(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.save()
            return redirect('CV')
    else:
        form = EducationForm()
    return render(request, 'cv_edit.html', {'name': 'Education', 'form': form})

def reference_new(request):
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.save()
            return redirect('CV')
    else:
        form = ReferenceForm()
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Reference'})

def personal_interests_new(request):
    if request.method == 'POST':
        form = PersonalInterestsForm(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = PersonalInterestsForm()
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Personal Interest'})

def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = ProjectForm()
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Project'})

def work_experience_new(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = WorkExperienceForm()
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Work Experience'})

def tech_skill_new(request):
    if request.method == 'POST':
        form = TechSkillForm(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = TechSkillForm()
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Technical Skill'})

def others_new(request):
    if request.method == 'POST':
        form = OthersForm(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.person = Person.objects.first()
            thing.save()
            return redirect('CV')
    else:
        form = OthersForm()
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Personal Other'})

def education_edit(request, pk):
    thing = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = EducationForm(instance=thing)
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Education'})

def reference_edit(request, pk):
    thing = get_object_or_404(Reference, pk=pk)
    if request.method == 'POST':
        form = ReferenceForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = ReferenceForm(instance=thing)
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Reference'})

def personal_interests_edit(request, pk):
    thing = get_object_or_404(PersonalInterests, pk=pk)
    if request.method == 'POST':
        form = PersonalInterestsForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = PersonalInterestsForm(instance=thing)
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Personal Interest'})

def project_edit(request, pk):
    thing = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = ProjectForm(instance=thing)
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Project'})

def work_experience_edit(request, pk):
    thing = get_object_or_404(WorkExperience, pk=pk)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = WorkExperienceForm(instance=thing)
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Work Experience'})

def tech_skill_edit(request, pk):
    thing = get_object_or_404(TechSkill, pk=pk)
    if request.method == 'POST':
        form = TechSkillForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = TechSkillForm(instance=thing)
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Technical Skill'})

def others_edit(request, pk):
    thing = get_object_or_404(Others, pk=pk)
    if request.method == 'POST':
        form = OthersForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.save()
            return redirect('CV')
    else:
        form = OthersForm(instance=thing)
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Personal Other'})

def person_edit(request):
    thing = get_object_or_404(Person, me=request.user)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.me = thing.me
            thing.save()
            return redirect('CV')
    else:
        form = PersonForm(instance=thing)
    return render(request, 'cv_edit.html', {'form': form, 'name': 'Personal Information'})