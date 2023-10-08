from django.shortcuts import render
from django.views import generic


index_template = 'core/index.html' 
project_template = 'core/project.html' 
about_template = 'core/about.html' 


class IndexView(generic.TemplateView):
    """
    """
    template_name = index_template

class AboutView(generic.TemplateView):
    """
    """
    template_name = about_template

class ProjectView(generic.TemplateView):
    """
    """
    template_name = project_template

