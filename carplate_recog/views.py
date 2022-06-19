import os

import cv2
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .detector import detector

TEMP_FILE_NAME = 'test.jpg'
det = detector()


@csrf_exempt
def recognize(request):
	# test_path = 'carplate_recog/demo_images'

	file = request.FILES['file']
	with open(TEMP_FILE_NAME, 'wb+') as fd:
		for chunk in file.chunks():
			fd.write(chunk)

	result = det.detect(cv2.imread(TEMP_FILE_NAME))

	return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})
