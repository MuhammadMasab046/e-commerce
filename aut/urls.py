from django.urls import path
from .views import signup, create_record, render_login_page, render_forgetpassword_page, send_password_reset_link,\
render_resetpassword_page, reset_password, user_profile, update_user_profile
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('create/', create_record, name='create_record'),
    path('login/', render_login_page, name='login'),
    path('forgetpassword/', render_forgetpassword_page, name='forgetpassword'),
    path('changepassword/', send_password_reset_link, name='changepassword'),
    path('resetpassword/<str:token>', render_resetpassword_page, name='resetpassword'),
    path('changepassword/<str:token>', reset_password, name='changepassword'),
    path('profile/', user_profile, name='profile'),
    path('updateprofile/', update_user_profile, name='updateprofile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]