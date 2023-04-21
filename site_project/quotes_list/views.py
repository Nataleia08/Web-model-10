from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'quotes_list/index.html')

@login_required
def create_author(request):
    if request.user.is_authenticated:
        return redirect(to='quotes_list:main')

    if request.method == 'POST':
        pass

    return render(request, 'users/login.html', context={"form": LoginForm()})