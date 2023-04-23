from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateQuoteForm, CreateAuthorForm
from .models import Authors, Quotes



# Create your views here.
def main(request):
    list = Quotes.object.all()
    return render(request, 'quotes_list/index.html')

@login_required
def create_author(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_list:main')
        else:
            return render(request, 'create_author.html', context={"form": form})

    return render(request, 'create_author.html', context={"form": CreateAuthorForm()})


@login_required
def create_quote(request):
    if request.method == 'POST':
        form = CreateQuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_list:main')
        else:
            return render(request, 'create_quote.html', context={"form": form})

    return render(request, 'create_quote.html', context={"form": CreateQuoteForm()})


def author_details(request, author_id):
    author = get_object_or_404(Authors, pk = author_id)
    return render(request, 'author_details.html', {"author": author})


# def next_page(request, number_page):
#     if request.method == "GET":
