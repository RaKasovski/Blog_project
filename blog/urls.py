from django.urls import path
from .import views

urlpatterns = [

	path('', views.showblog, name="shbg"),
	path('<int:post_id>/', views.specific_post, name='specific_post'),
]
