# Create your views here.
import os
from abc import ABC

from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView

from waitlist.forms import UserDetailForm, UserDataForm


class IndexView(TemplateView):
    template_name = 'index_view.html'
    pass


class WaitListView(SessionWizardView, ABC):
    template_name = 'waitlist_view.html'
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))
    form_list = [UserDataForm, UserDetailForm]
    success_url = reverse_lazy('waitlist:waitlist_success')

    def done(self, form_list, **kwargs):
        user_data_form = form_list[0]
        user_detail_form = form_list[1]
        user_data = user_data_form.save()
        user_detail = user_detail_form.save(commit=False)
        user_detail.user = user_data
        user_detail.save()

        messages.success(self.request, f'Your details have been captured')
        return redirect('waitlist:waitlist_success')


class WaitListSuccessView(TemplateView):
    template_name = 'waitlist_success_view.html'
    pass
