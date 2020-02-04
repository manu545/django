from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import View
from django.template import context
from django.contrib.auth import login, authenticate, forms
from django.contrib.auth.decorators import login_required
from usrprofil.forms import UserForm, ProfileForm, UserCreateForm
from django.template import RequestContext

@login_required()
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/user/profileupdated')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', context={'user_form': user_form,'profile_form': profile_form})

class Register(View):
    form = UserCreateForm
    def get(self, request):
        context = {'form' : self.form()}
        return render(request, 'reg.html', context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks')
        else:
            context = {'form' : form}
            return render(request, 'reg.html', context)

# Create your views here.
def search(request):
    if request.method== 'GET':
        search_id=request.POST['txtSearch']
        for p in ProfileForm.objects.raw("SELECT * FROM Profiles_Profile where user=%s",[search_id]):
            list.append(p)
            return render(request,'test.html',context={'value1':p})
