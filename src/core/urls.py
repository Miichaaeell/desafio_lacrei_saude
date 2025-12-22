from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    #Urls for consultations
    path('api/consultations/', views.ConsultationListCreateAPIView.as_view(), name='consultation'),
    path('api/consultations/<int:pk>/', views.ConsultationRetrieveUpdateDestroyAPIView.as_view(), name='consultation'),
    
    #Urls for professionals
    path('api/professionals/', views.ProfessionalListCreateAPIView.as_view(), name='professional'),
    path('api/professionals/<int:pk>/', views.ProfessionalRetrieveUpdateDestroyAPIView.as_view(), name='professional'),
    
    #URLS for authentication
    path('api/authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]