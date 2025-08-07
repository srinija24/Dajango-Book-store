from django.urls import path
from .views import BookCheckoutView, BooksListView,BookDetailView
urlpatterns=[
    path("",BooksListView.as_view(),name="list"),
    path("<int:pk>/",BookDetailView.as_view(),name="detail"),
    path("<int:pk>/checkout/",BookCheckoutView.as_view(),name="checkout"),
]