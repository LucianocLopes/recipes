# from django.shortcuts import render
# from django.views import View
from django.views.generic import TemplateView

# def home(request):
#     return render(request, 'recipes/pages/home.html')


# class HomeView(View):
    
#     def render_recipe(self):
        
#         return render(
#             self.request,
#             'recipes/pages/home.html',
#             context={
                
#             }
#         )

#     def get(self, request):
#         return self.render_recipe()


class HomeView(TemplateView):
    template_name = 'recipes/pages/home.html'
