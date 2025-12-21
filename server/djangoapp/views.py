BACKEND_URL = "https://varadnakhate-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_dealers(request):
    try:
        url = BACKEND_URL + "/dealers"
        response = requests.get(url)
        response.raise_for_status()
        return JsonResponse(response.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)})


@csrf_exempt
def get_dealers_by_state(request, state):
    try:
        url = BACKEND_URL + "/dealers"
        response = requests.get(url, params={"state": state})
        response.raise_for_status()
        return JsonResponse(response.json(), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)})
