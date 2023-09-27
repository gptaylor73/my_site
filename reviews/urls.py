from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you', views.ThankYouView.as_view(), name='thank-you'),
    path('reviews-list', views.ReviewsListView.as_view()),
    path('<int:pk>/', views.ReviewDetailView.as_view())
]
