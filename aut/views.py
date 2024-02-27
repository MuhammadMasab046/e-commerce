from django.shortcuts import render, redirect
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework import status
from .forms import UserForm
from .serializers import UserSerializer,PasswordSerializer, UserProfileSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
import jwt


from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Imports for send the email links.
from django.core.mail import send_mail

from django.core.mail import send_mail

from rest_framework.permissions import IsAuthenticated

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['name'] = user.name
#         # ...

#         return token
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer



def signup(request):

    # user = User.objects.get(email='masab.akram@tiksom.com')

    # # Check if a provided password matches the stored (hashed) password
    # print(user.password)
    # if check_password('masab', user.password):
    #     # Passwords match
    #     print("Passwords match!")
    # else:
    #     # Passwords do not match
    #     print("Passwords do not match.")

    return render(request, "signup.html")
    #return render(request, 'aut/userform.html')


#def create_record(request):
    # if request.method == 'POST':
    #     serializer = UserSerializer(data=request.data)
    #     print("data---")
    #     email = unquote(request.POST.get('email'))
    #     print("emil--",email)
    #     if serializer.is_valid():
    #         #raw_password = request.POST['password']
    #         #hashed_password = make_password(raw_password)
    #         #print("password--",hashed_password)
    #         #user = User.objects.create(serializer, password=hashed_password)
    #         user = User.objects.create_user(**serializer.validated_data)
    #         user.save()
    #         #serializer.save()
    #         return Response({'message': 'Record created successfully'}, status=status.HTTP_200_OK)
    #     print("data valid--not")
    #     return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_record(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return Response({'message': 'Record created successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def render_login_page(request):
    return render(request, "login.html")  

def render_forgetpassword_page(request):
    return render(request, "forgetpassword.html")  

# @api_view(['POST'])
# @csrf_exempt
# @require_POST
# def send_password_reset_link(request):
#     # Get the email from the request data
#     email = request.POST.get('email')

#     # Check if the email exists
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         # If the email does not exist, return an error response
#         return JsonResponse({'error': 'Email does not exist'}, status=400)

#     # Generate a password reset token
#     current_site = get_current_site(request)
#     subject = 'Password Reset Request'
#     message = render_to_string('signup.html', {
#         'user': user,
#         'domain': current_site.domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': default_token_generator.make_token(user),
#         'protocol': 'https' if request.is_secure() else 'http',
#     })

#     # Send the password reset email
#     send_mail(subject, message, 'masab.akram@tiksom.com', [user.email])

#     return JsonResponse({'success': 'Password reset link sent successfully'})

@api_view(['POST'])
def send_password_reset_link(request):
    # Get the email from the request data
    email = request.data.get('email')

    # Check if the email exists
    user = User.objects.filter(email=email).first()
    if user != None:
        #user = get_object_or_404(User, email=email)
        #token = default_token_generator.make_token(user)
        refresh = RefreshToken.for_user(user)
        access: str(refresh)
        token = str(refresh.access_token),
        print("token---",refresh.access_token)

        # Generate a password reset token
        current_site = get_current_site(request)
        send_mail(
        subject='Reset password link',
        #message='http://127.0.0.1:8000/auth/resetpassword/'+ str(token),
        message='http://127.0.0.1:8000/auth/resetpassword/'+str(refresh.access_token),
        from_email='masab.akram@tiksom.com',
        recipient_list=[user.email])
        # Send the password reset email
        #send_mail(subject, message, 'masab.akram@tiksom.com', [user.email])

        return Response({'success': 'Password reset link sent successfully', 'type':'success'})
    else:
        return Response({'success': 'Password reset link sent successfully', 'type':'errors'})

# @api_view(['GET'])
# def render_resetpassword_page(request, token):
#     #decodedPayload = jwt.decode(token,None,None)
#     #print("----------token-----",decodedPayload)
#     return render(request, "resetpassword.html", {'token': token})
#     #return render(request, "resetpassword.html", {'token': token}) 
def render_resetpassword_page(request, token):
    try:
        refresh = RefreshToken(token)
        print("Decoded Token: ", refresh)
    except Exception as e:
        print("Token Decoding Error: ", e)

    return render(request, "resetpassword.html", {'token': token}) 

@api_view(['POST'])
def reset_password(request, token):
    if request.method == 'POST':
        decodedPayload = jwt.decode(token, None, None)
        user_id = decodedPayload['user_id']
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
           # data = serializer.save()
            user = User.objects.get(id=user_id)
            print("user----",user)
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'success': 'Password reset successfully', 'type':'success'})




# @api_view(['POST'])
# def generate_token(request):
#     if request.method == 'POST':
#         email = request.data['email']
#         password = request.data['password']

#         print(email)
#         print(password)

#         user = authenticate(email=email, password=password)
#         print("---", user)

#         if user is not None:
#             print("afjljfhfhfh")
#             refresh = RefreshToken.for_user(user)
#             #print("-------l--", refresh)

#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),  # Convert access_token to a string
#             })
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#     return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)






# @api_view(['POST'])
# def login_api(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     user = User.objects.get(email=email)

#     # Check if a provided password matches the stored (hashed) password
#     print(user.password)
#     if check_password(password, user.password):
#         # Passwords match
#         print("Passwords match!")
#     else:
#         # Passwords do not match
#         print("Passwords do not match.")

#     user = authenticate(email=email, password=password)

#     if user:
#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)

#         return Response({
#             'access_token': access_token,
#             'user': UserSerializer(user).data
#         }, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    # print(request.user.is_authenticated)  # Debugging line
    #return Response({"sucess":"success"})
    try:
        user = request.user
        # Check if the user has an email attribute (is authenticated)
        if hasattr(user, 'email'):
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'User is not authenticated'}, status=403)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user

    if request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)    