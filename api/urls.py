from django.urls import path
from .views import CreateCustomerView, UserView
urlpatterns = [
    path("customer/", CreateCustomerView.as_view()),
    path("user/", UserView.as_view())
]
