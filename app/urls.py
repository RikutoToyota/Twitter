from django.urls import path
from . import views
from .views import thread_list, view_thread, post


app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('threads/', thread_list, name='thread_list'),

    path('threads/<int:thread_id>/', view_thread, name='view_thread'),
    path('thread_save/',post, name='thread_save' ),
    path('threads/<int:thread_id>/comment/', views.come_post, name="comment")
]