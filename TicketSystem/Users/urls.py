from django.urls import path
from . views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', getRoutes, name='routes'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add_ticket',add_ticket,name='add_ticket'),
    path('get_ticket_by_user/<str:email>',get_ticket_by_user,name='get_ticket_by_user')
]
