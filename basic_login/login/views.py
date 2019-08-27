from django.shortcuts import render
from django.template import Template
from django.contrib.auth.decorators import login_required


from .forms import loginForm

# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         form = loginForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/login/success')
#     else:
#         form = loginForm()

#     return render(request,'login/index.html', {'form': form})

@login_required(login_url='login')
def success(request):
    return render(request,'registration/success.html')
