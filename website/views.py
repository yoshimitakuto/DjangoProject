from typing import Any, Dict
from django.views.generic import TemplateView  #djangoがもともと用意しているview(TemplateViewを使うことでユーザー画面に表示させることができる)

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['username'] = 'takuto'
        return ctxt
        
class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['num_servies'] = 3344555
        ctxt['skils'] = [
            "Ruby(RubyOnRails)",
            "Python(Django)",
            "Javascript(Jquery)"
        ]
        return ctxt 