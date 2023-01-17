from  django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from .sent_mail import send_confirmation_email
from . import serializers

User = get_user_model()


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                try:
                    send_confirmation_email(user.email, user.activation_code)
                except:
                       return Response({
                            'msg': 'Registered bit troubles with mail',
                           'data': serializer.data}, status=201)
                return Response(serializer.data, status=201)
            return Response('Bad request!', status=400)

class ActicationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, activation_code):
        try:
            User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({
                'msg': 'seccsesfully activated!'
            }, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'link expired!'}, status=400)