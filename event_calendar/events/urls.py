from . import views
from django.urls import path

app_name = 'calendar'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_event', views.new_event, name='new_event'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('details/<int:id>', views.details, name='details'),
    path('update/<int:id>', views.update, name='update'),
    path('log_in', views.log_in, name="log_in"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('log_out', views.log_out, name="log_out"),
]