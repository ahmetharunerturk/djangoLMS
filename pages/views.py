from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["courses"] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_course']= Course.objects.filter(available=True).count()
        return context
    



# def index(request):
#     return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')

class AboutView(TemplateView):
    template_name = 'about.html'