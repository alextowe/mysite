from django.shortcuts import render
from django.views.generic import TemplateView


index_template = 'core/index.html' 
portfolio_template = 'core/portfolio.html' 
about_template = 'core/about.html' 


class IndexView(TemplateView):
    """
    """
    template_name = index_template

class AboutView(TemplateView):
    """
    """
    template_name = about_template

class PortfolioView(TemplateView):
    """
    """
    template_name = portfolio_template

