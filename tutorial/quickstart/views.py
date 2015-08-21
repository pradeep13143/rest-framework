from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from django.http import JsonResponse
from rest_framework import generics as g

#

class JsonManager(object):

    def get_mdl(self):
        return User

    #  JsonManager
    def get_queryset(self):
        mdl = self.get_mdl()
        return mdl.objects.all()

    #  JsonManager
    def get_serializer_class(self):
        return UserSerializer

    #  JsonManager
    def get_object(self):
        qs = self.get_queryset()
        return qs.get(id=self.kwargs.get('object_id'))


class AddUser(JsonManager, g.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.POST['password'])




from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
'''
@api_view(['POST'])
@csrf_exempt
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)'''


'''

@csrf_exempt
def register(request, template_name='register.html',
             register_form=UserCreationForm,
             current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = "/success/"
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to)
    else:
        form = register_form(request)

    context = {
        'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)

def success(request):
    template_name = 'success.html'
    context = {'msg':"Registered Successfully"}
    return TemplateResponse(request, template_name, context)'''
