from rest_framework import generics

from student.models import StudentProfile

from .serializers import StudentSerializer



class StudentAPIView(generics.ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer


class StudentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer

class StudentAPINewView(generics.ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    #queryset = StudentProfile.objects.all().order_by('-id')[:1] # latest quote
    serializer_class = StudentSerializer
