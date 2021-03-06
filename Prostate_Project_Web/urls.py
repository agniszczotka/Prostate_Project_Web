from django.conf.urls import patterns, url, include


from django.contrib import admin
from profiles.forms import SignupFormExtra

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^project/', include('project_info.urls')),
    url(r'^project/', include('DataBase.urls')),
    url(r'^$', 'Prostate_Project_Web.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/about/$','django.contrib.flatpages.views.flatpage',{'url':'/project/about/'},name='about'),

    # Demo Override the signup form with our own, which includes a
    # institution
    url(r'^accounts/signup/$','userena.views.signup',{'signup_form':SignupFormExtra }),
    url(r'^accounts/', include('userena.urls')),

    #(r'^i18n/', include('django.conf.urls.i18n')),
)

# Add media and static files
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'Prostate_Project_Web.views.handler404'
handler400 = 'Prostate_Project_Web.views.handler400'
handler500 = 'Prostate_Project_Web.views.handler500'

