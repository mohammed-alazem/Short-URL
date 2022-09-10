from django.shortcuts import render, get_object_or_404  # We will use it later
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Shortener
from .forms import ShortenerForm


# Create your views here.

def home_view(request):
    template = 'urlshortener/home.html'

    context = {'form': ShortenerForm()}

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.ShortURL

            long_url = shortened_object.LongURL

            context['new_url'] = new_url
            context['LongURL'] = long_url

            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(ShortURL=shortened_part)

        shortener.UsedCount += 1

        shortener.save()

        return HttpResponseRedirect(shortener.LongURL)

    except:
        raise Http404('Sorry this link is broken :(')
