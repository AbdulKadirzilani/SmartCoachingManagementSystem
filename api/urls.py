from django.urls import path



from .views import StudentAPIView,StudentAPIDetailView,StudentAPINewView

urlpatterns = [
   # path('', QuoteCategoryAPIView.as_view()),
   # path('quotes/', QuoteAPIView.as_view()),

    path('', StudentAPIView.as_view()),

    path('student/<int:pk>/', StudentAPIDetailView.as_view()),
    path('student/new/', StudentAPINewView.as_view()),


]