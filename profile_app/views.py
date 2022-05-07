from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profile
from .forms import ProfileUpdateForm


def profile_page(request, user_username):
    target_user = get_object_or_404(User, username=user_username)
    context = {
        'target_user': target_user,
    }
    return render(request, 'profile_app/profile.html', context)


def profile_update_page(request, user_username):
    logged_user = get_object_or_404(User, username=user_username)
    own_profile, is_created = Profile.objects.get_or_create(user_id=logged_user.id)
    profile_form = ProfileUpdateForm(instance=own_profile)

    if request == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=own_profile)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.save()
            context = {
                'target_user': logged_user
            }
            return redirect('/')
        else:
            return HttpResponse("is_valid == False")

    context = {
        'own_profile': own_profile,
        'form': profile_form,
    }
    return render(request, 'profile_app/profile_update.html', context)

# class ProfileCreateView(CreateView):
#     model = Profile
#     context_object_name = 'target_profile'
#     form_class = ProfileCreationForm
#     success_url = reverse_lazy('profile:profile')
#     template_name = 'profile_app/profile_create.html'
#
#     def form_valid(self, form):
#         temp_profile = form.save(commit=False)
#         temp_profile.user = self.request.user
#         temp_profile.save()
#         return super().form_valid(form)
