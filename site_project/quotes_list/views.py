from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateQuoteForm, CreateAuthorForm
from .models import Authors, Quotes, Tag



# Create your views here.
def main(request):
    quotes_list = Quotes.objects.all()
    return render(request, 'quotes_list/index.html', {"quotes_list": quotes_list})

@login_required
def create_author(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_list:main')
        else:
            return render(request, 'quotes_list/create_author.html', context={"form": form})

    return render(request, 'quotes_list/create_author.html', context={"form": CreateAuthorForm()})


@login_required
def create_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = CreateQuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to='quotes_list:main')
        else:
            return render(request, 'quotes_list/create_quote.html', {"tags": tags, 'form': form})

    return render(request, 'quotes_list/create_quote.html', {"tags": tags, 'form': CreateQuoteForm()})

def author_details(request, author_id):
    author = get_object_or_404(Authors, pk = author_id)
    return render(request, 'quotes_list/author_details.html', {"author": author})


# def next_page(request, number_page):
#     if request.method == "GET":


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/tag.html', {'form': form})

    return render(request, 'noteapp/tag.html', {'form': TagForm()})