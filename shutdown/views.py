from django.shortcuts import render
from django.http import JsonResponse
import os
from kvantoriumdjango import dataadmin as admin

"""
IT KVANTUM Отключение компов.
"""

listit = [
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
    for pc in listit:
        os.system(r"net rpc -S {} -U 'KVANTORIUM\{}%{}' shutdown -t 1 -f".format(pc, admin.user, admin.password))
    return JsonResponse({"isShutDown": True})


"""
HITECH KVANTUM Отключение компов.
"""

listhitech = [
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

def shutdown_hitech(request):
    for pc in listhitech:
        os.system(r"net rpc -S {} -U 'KVANTORIUM\foksha.as%P@ssw0rd' shutdown -t 1 -f".format(pc))
    return JsonResponse({"isShutDown": True})