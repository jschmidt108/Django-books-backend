from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/reviews', views.ReviewList.as_view(), name='review_list'),
    path('api/reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),

]