#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging

from .models import Post
from .models import Course_table

logger = logging.getLogger('django')

# Create your views here.
# class HelloAPIView(APIView):
#     def get(self, request):
#         my_name = request.GET.get('name' , None)
#         if my_name:
#             retValue = {}
#             retValue['data'] = "Hello" + my_name
#             return Response(retValue, status=status.HTTP_200_OK)
#         else:
#             return Response(
#                 {"res": "paramete: name is None"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
@api_view(['GET'])
def add_post(request):
    title = request.GET.get('title' , '')
    content = request.GET.get('content' , '')
    photo = request.GET.get('photo' , '')
    location = request.GET.get('location' , '')


    new_post = Post() 
    new_post.title = title
    new_post.content = content
    new_post.photo = photo
    new_post.location = location
    new_post.save()
    logger.debug(" ************* myhello_api:"+ title)
    if title:
        return Response({"data": title + " insert!"}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"res": "parameter: name is None"},
            status=status.HTTP_400_BAD_REQUEST
        )  

@api_view(['GET'])
def addcourse_course(request):
    Department = request.GET.get('Department' , '')
    CourseTitle = request.GET.get('CourseTitle' , '')
    Instructor = request.GET.get('Instructor' , '')

    new_course = Course_table()
    new_course.Department = Department
    new_course.CourseTitle = CourseTitle
    new_course.Instructor = Instructor
    new_course.save()         
    
@api_view(['GET'])
def list_post(request):
    posts = Post.objects.all().values()
    return JsonResponse(list(posts), safe=False)

@api_view(['GET'])
def courselist_course(request):
    posts = Course_table.objects.all().values()
    return JsonResponse(list(posts), safe=False)
    # return Response({"data": 
    #     json.dumps(
    #         list(posts),
    #         sort_keys=True,
    #         indent=1,
    #         cls=DjangoJSONEncoder)},
    #     status=status.HTTP_200_OK
    # )
