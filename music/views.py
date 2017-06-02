# -*- coding: utf-8 -*-
import operator

from crispy_forms.layout import HTML
from django.core import paginator
from django.core.mail import BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, request
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
# 在每一个页面上保持你的登陆信息
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View
from .models import Album,SignUp,Song
from .forms import UserForm, SignUpForm, ContactForm, SongForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Album
from django.template import loader
from django.contrib import messages
import django_filters
from requests import *


class Search(generic.ListView):
    model = Album
    template_name = 'music/index.html'

    def get_queryset(self):
        result = Album.objects.all()
        # result = super(Search, self).get_queryset()

        query = self.request.GET.get('q')
        a = "in"
        if query:
            result=result.filter(
                Q(driver__username__contains=query) |
                Q(path__contains=query) |
                Q(location__contains=query)
                  )
            query_list = query.split()
        #     result = result.filter(
        #         reduce(operator.and_,
        #                (Q(title__icontains=q) for q in query_list)) |
        #         reduce(operator.and_,
        #                (Q(content__icontains=q) for q in query_list))
        #     )

        # return Album.objects.filter(driver__username__contains=query)
            return result
        return result









def contact(request,pk,pk2):
        form = ContactForm(request.POST or None)
        alb = Album.objects.get(pk=pk)
        sta = Song.objects.get(pk=pk2)
        driver = alb.driver
        if form.is_valid():

            e_1=alb.driver.email
            form_message = form.cleaned_data.get("message")
            name = request.user.username
            user_email = request.user.email
            # print (email,message,full_name)
            subject = 'Pick Me Up !'
            from_email = settings.EMAIL_HOST_USER
            to_email = [e_1]
            contact_message = "User %s: %s with email address:  %s"%(
                name,
                form_message,
                user_email,
                )

            some_html_message =render_to_string(
                'music/email.html',
                {'driver': driver,
                 'user': name,
                 'email':user_email,
                 'words':form_message,
                 'station':sta.station,
                 'time':sta.time,
                 'location':alb.location
                 })

            if subject and contact_message and from_email:
                try:
                    send_mail(subject,
                              some_html_message,
                              from_email,
                              to_email,
                              html_message=some_html_message,
                              fail_silently=True)
                    messages.success(request,"Successfull Sent")
                    url = str('/music/') + str(pk)
                    return HttpResponseRedirect(url)

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

        context = {
            "form": form,
            "Location":sta.location.location,
            "Station":sta.station,
            "Time":sta.time,
            "Driver":driver
        }
        return render(request,"music/forms.html",context)


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()



class Mine(generic.ListView):
    template_name = 'music/mine.html'

    # 更改object.all()名字
    # context_object_name ="all_albums"

    def get_queryset(self):
        return Album.objects.all()




class SignUpView(SignUp):
    model = SignUp
    fields = ['full_name','email']


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['location','path','photo']

    def form_valid(self, form):
        driver = self.request.user
        form.instance.driver = driver
        return super(AlbumCreate,self).form_valid(form)


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['location', 'path', 'photo']



class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class StationCreate(CreateView):
    template_name = 'music/song_form.html'
    form_class = SongForm

    def get_form_kwargs(self):
        kwargs = super(StationCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs





class StationUpdate(UpdateView):
    model = Song
    fields = ['station', 'time', 'is_full']

class StationDelete(DeleteView):
    model = Song

    # def delete(self, request, *args, **kwargs):
    #
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)

    def get_success_url(self):
        post = self.object.location
        return reverse_lazy('music:detail',kwargs={'pk':post.id})

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form': form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)


        if form.is_valid():

            user = form.save(commit=False)

            #cleaned(normalized)data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})