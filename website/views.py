from django.views.generic import TemplateView  #djangoがもともと用意しているview(TemplateViewを使うことでユーザー画面に表示させることができる)

class IndexView(TemplateView):
    template_name = 'index.html'
    
class AboutView(TemplateView):
    template_name = 'about.html'    