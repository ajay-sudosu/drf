from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def studentapi(request):
	if request.method == "GET":
		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		id=pythondata.get('id',None)
		if id is not None:
			stu=Student.objects.get(id=id)
			serializer=StudentSerializer(stu)
			json_data=JSONRenderer().render(serializer.data)
			return HttpResponse(json_data,content_type='application/json')
		stu=Student.objects.all()
		serializer=StudentSerializer(stu,many=True)
		json_data=JSONRenderer().render(serializer.data)
		return HttpResponse(json_data,content_type='application/json')

	if request.method=="POST":
		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		serializer=StudentSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res={'msg':'data posted'}
			json_data=JSONRenderer().render(res)
			return HttpResponse(json_data,content_type='application_data')
		json_data=JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type='application_data')

	if request.method=="PUT":
		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		id=pythondata.get('id',None)
		stu=Student.objects.get(id=id)
		serializer=StudentSerializer(stu,partial=True,data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res={'msg':'data posted'}
			json_data=JSONRenderer().render(res)
			return HttpResponse(json_data,content_type='application_data')
		json_data=JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type='application_data')

	if request.method=='DELETE':
		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		id =pythondata.get('id')
		stu=Student.objects.get(id=id)
		stu.delete()
		res={'msg':'data deleted'}
		json_data=JSONRenderer().render(res)
		return HttpResponse(json_data,content_type='application_data')
		