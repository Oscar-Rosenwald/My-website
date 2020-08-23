from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User

from home.models import Post
from home.forms import PostForm

from home.models import Person

from home.models import Education

from home.models import TechSkill

from home.models import WorkExperience

from home.models import PersonalInterests

from home.models import Reference

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
    others = person.personal_others

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

    return render(request, 'CVs.html', {'tech_skills': tech, 'work_experience': exp, 'personal_interests': interests, 'references': refs, 'education': education, 'name': name, 'email': email, 'address': address, 'phone_number': phone_number})

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

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = PostForm(request.POST, pk=post.pk)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
