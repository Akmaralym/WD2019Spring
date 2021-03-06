from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import status
from .models import Contact
from django.contrib.auth.models import User
from .serializer import UserSerializer, ContactSerializer
from rest_framework.permissions import IsAuthenticated




@csrf_exempt
def contact(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = ContactSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad response'})

class contact_lists(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Contact.objects.for_user_order_by_name(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)





@csrf_exempt
def detail_contact(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    # if request.method == 'GET':
    #     serializer = ContactSerializer(contact)
    #     return JsonResponse(serializer.data)
    if request.method == 'PUT':
        body = json.loads(request.body)
        serializer = ContactSerializer(instance=contact, data=body)
        if serializer.�~c��\����G���>��np�O�%i�5�V1���1�S�fg�u������&���]51�J��G=�ҝo�Su��)�$��2�T�zk[n�����à�K��B��P�ϋQYn���9�/�P���@�����r�7UNzw��b�s��f���E����������Y���v3q��ј:���e���R�Y�����k�����B~K8kzoJ�g������*�-�5n��+7Ux=xg���\�0�Fb�0ag>��8:���M��փ��	�T��UB���@�@��.ţa菀����]$�A�	�l�K�C�{P���4ԭ M�N�Gg�ԇ_Cþвf�T��=7ף1�>9m
82�[��<��:����\G�e��(7{ƵFQ���ǜDe#_��4Q�2"`IQɭل��5�`�om���FN�O�I���[8����n����G����[��6�|8��������E��'�T]����7z\�ÂӲPK�$�}��]=�����'|�V����0n����� �)�YH���<�M��n���s�q�	�C�
�UE�A��v�K������T�h�v�q}$��Y��l��O2K�M5���z{����,;��UQ?nV}B�4}ܴ%�=˸(�rЖ!����7U��.k�p 3����r�NO�ZUd�I���no�?e!�ǶZl����jh���>T��wX�ě�=��kMM�hϒ5_��߇OCP��*W� #�g)�]2X:Y��e1Ќ-y?͵JGc���IY���Z!���q)n�eʛ�ydy%�A�L��T��	Xs���ǹ�hx!c>c��^L��?��������ҽ&�('w����o'��a%�\a�M�w0N(�.n��Ώ���G�oTj��l�E���g2�