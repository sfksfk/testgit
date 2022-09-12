from django.shortcuts import render

# Create your views here.


from django.views.generic.base import View

# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'userapp/register.html')