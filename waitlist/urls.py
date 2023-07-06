from django.urls import path

from waitlist.views import IndexView, WaitListView, WaitListSuccessView

app_name = 'waitlist'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('waitlist/', WaitListView.as_view(), name='join_waitlist'),
    path('waitlist/success/', WaitListSuccessView.as_view(), name='waitlist_success')
]
