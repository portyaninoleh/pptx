from django.conf.urls import patterns, include, url

from pptxApp.views import PresentationsListView
from pptxApp.views import UploadPresenation

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pptxConverter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PresentationsListView.as_view(),
        name='show_presentations'),
    url(r'^upload/$', UploadPresenation.as_view(),
        name='upload_presentation'),
)
