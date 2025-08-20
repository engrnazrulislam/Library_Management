from books import views
from django.urls import path, include
urlpatterns = [
    path('<int:id>', views.ViewSpecificBook.as_view(), name='product-list')
]