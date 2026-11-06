from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

from .models import CustomUser
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Your account has been created successfully! You can now log in."
        )
        return response


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "accounts/profile.html"
    fields = ["first_name", "last_name", "email", "course"]
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user
