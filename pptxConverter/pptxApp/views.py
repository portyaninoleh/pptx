from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from presentation_handler import PresentationHandler

from models import Presentation
from models import PresentationImages


class PresentationsListView(View):

    def get(self, request):
        title = request.GET.get('title', False)
        if not title:
            return render(request, 'presentations_list.html', {'error': True})
        presentation = Presentation.objects.get(title=title).presentationimages_set.all()
        return render(request, 'presentations_list.html', {'presentation': presentation})


class UploadPresenation(View):

    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        presentation_converted = PresentationHandler(request.POST, request.FILES)
        presentation = Presentation(title=presentation_converted.title,
                                   presentation=presentation_converted.path['presentation'])
        presentation.save()
        for i in range(len(presentation_converted.path['images'])):
            presentation.presentationimages_set.add(PresentationImages(image=presentation_converted.path['images'][i],
                                                                       image_min = presentation_converted.path['thumbnail'][i]))
        presentation.save()
        return HttpResponseRedirect(reverse('upload_presentation'))
