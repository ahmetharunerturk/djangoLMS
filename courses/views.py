from django.shortcuts import render, get_object_or_404
from .models import Course, Category, Tag


# def course_list(request):
#     courses = Course.objects.all().order_by('-date')
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {
#         'courses': courses,
#         'categories': categories,
#         'tags': tags
#     }   

#     return render(request, 'courses.html', context)

def course_list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories=Category.objects.all()
    tags = Tag.objects.all()
    current_user = request.user
    
    
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(available=True, category=category_page)
        
    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter(available=True, tags=tag_page)
        
    else:
       
        
        if current_user.is_authenticated:
            enrolled_courses = current_user.courses_joined.all()
            courses = Course.objects.all().order_by('-date')
            for course in enrolled_courses:
                courses = courses.exclude(id=course.id)
        else:
           courses = Course.objects.all().order_by('-date')         
            
            
    context = {
         'courses': courses,
         'categories': categories,
         'tags': tags
     }   

    return render(request, 'courses.html', context)

def course_detail(request, category_slug, course_id):
    current_user = request.user
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    courses = Course.objects.all().order_by('-date')  
    categories=Category.objects.all()
    tags = Tag.objects.all()
        
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()
    else:
        enrolled_courses = courses
        
    categories = Category.objects.all()
    
    context = {
        'course': course,
        'categories': categories,
        'tags': tags,
        'enrolled_courses': enrolled_courses,
    }

    return render(request, 'course.html', context)

def category_list(request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    tags = Tag.objects.all()
    context = {
        'courses': courses,
        'tags': tags
    }

    return render(request, 'courses.html', context)

def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug)
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'tags': tags
    }

    return render(request, 'courses.html', context)

def search(request):
    courses = Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'courses': courses,
        'tags': tags
    }

    return render(request, 'courses.html', context)


