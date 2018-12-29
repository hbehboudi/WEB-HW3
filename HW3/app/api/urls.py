from django.conf.urls import url
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework_simplejwt import views as jwt_views



router = routers.DefaultRouter()

urlpatterns = [
    path('v1/tweet/', views.TweetList.as_view()),
    path('v1/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v2/tweet/', views.TweetList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
