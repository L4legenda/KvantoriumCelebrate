from django.shortcuts import render
from django.http import JsonResponse
import os

listpc = [
    "pc-it01",
    "pc-it02",
    "pc-it03",
    "pc-it04",
    "pc-it05",
    "pc-it06",
    "pc-it07",
    "pc-it08",
    "pc-it09",
    "pc-it10",
    "pc-it11",
    "pc-it12",
    "pc-it13",
    "pc-it14",
    "pc-it15",
    "pc-it16",
    "pc-it17",
    "pc-it18"
]

# Create your views here.
def shutdown_it(request):
    for pc in listpc:
        os.system(r"net rpc -S {} -U 'KVANTORIUM\foksha.as%P@ssw0rd' shutdown -t 1 -f".format(pc))
    return JsonResponse({"isShutDown" : True})