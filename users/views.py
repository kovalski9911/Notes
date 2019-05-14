from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import UserRegisterForm


class UserRegisterView(FormView):
    """User registration view"""

    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.save()
        return super(UserRegisterView, self).form_valid(form)
