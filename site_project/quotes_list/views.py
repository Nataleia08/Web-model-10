from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateQuoteForm, CreateAuthorForm, TagForm
from .models import Authors, Quotes, Tag
from django.core.paginator import Paginator
import json




# Create your views here.
def main(request, page = 1):
    quotes_list = Quotes.objects.all()
    per_page = 10
    paginator = Paginator(quotes_list, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes_list/index.html', context={"quotes_list": quotes_on_page})

@login_required
def create_author(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_list:main')
        else:
            return render(request, 'quotes_list/create_author.html', context={"form": form, "message": "Author not created!"})

    return render(request, 'quotes_list/create_author.html', context={"form": CreateAuthorForm()})


@login_required
def create_quote(request):
    tags = Tag.objects.all()
    authors = Authors.objects.all()


    if request.method == 'POST':
        form = CreateQuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            # choice_author = Authors.objects.filter(fullname__in=request.POST.getlist('authors'))
            # new_quote.author = choice_author
            form.fields["author"].queryset = Authors.objects.filter(fullname=form.cleaned_data['author'])

            return redirect(to='quotes_list:main')
        else:
            return render(request, 'quotes_list/create_quote.html', context={"tags": tags, "authors": authors, 'form': form, "message": "Quotes not created!"})

    return render(request, 'quotes_list/create_quote.html', context={"tags": tags, "authors": authors, 'form': CreateQuoteForm()})

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
            return redirect(to='quotes_list:main')
        else:
            return render(request, 'quotes_list/tag.html', context={'form': form, "message": "Tag not created!"})

    return render(request, 'quotes_list/tag.html', context={'form': TagForm()})

def tags_list(request, tag_id):
    quotes = Quotes.objects.all()
    return render(request, 'quotes_list/tags_list.html', context={"quotes": quotes})

def top_ten_tags(request):
    top_tags = Tag.objects.all()[:9]
    return render(request, "quotes_list/index.html", context={"top_tags":top_tags})

@login_required
def script(request):
    with open("script/authors.json") as fh:
        authors = json.load(fh)

    for author in authors:
        Authors.objects.get_or_create(fullname=author["fullname"], born_date=author["born_date"],
                                      born_location=author["born_location"], description=author["description"])

    with open("script/quotes.json") as fh:
        quotes = json.load(fh)

    for quote in quotes:
        tags = []
        for tag in quote["tags"]:
            t, *_ = Tag.objects.get_or_create(name=tag)
            tags.append(t)
        exist_quote = bool(len(Quotes.objects.filter(quote=quote["quote"])))

        if not exist_quote:
            author = db.authors.find_one({"_id": quote['author']})
            au = Authors.objects.get(fullname=author["fullname"])
            qu = Quotes.objects.create(quote=quote['quote'], author=au)
            for tag in tags:
                qu.tags.add(tag)

    # with open("script/user_list.json") as fh:
    #     user_list = json.load(fh)
    #
    # for us in user_list:
    #     UsersSite.objects.get_or_create(nickname=us["fullname"], email=us["email"],
    #                                     phone=us["phone"], login=us["email"])

    return redirect(to='quotes_list:main')
