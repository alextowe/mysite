from django.shortcuts import render
from django.views import generic


index_template = 'core/index.html' 
portfolio_template = 'core/portfolio.html' 
about_template = 'core/about.html' 


class IndexView(generic.TemplateView):
    """
    """
    template_name = index_template

class AboutView(generic.TemplateView):
    """
    """
    template_name = about_template

class PortfolioView(generic.TemplateView):
    """
    """
    template_name = portfolio_template

