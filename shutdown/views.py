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
]

# Create your views here.
def shutdown_it(request):
    for pc in listit:
        os.system(r"net rpc -S {0} -U 'KVANTORIUM\{1}%{2}' shutdown -t 1 -f".format(pc, admin.user, admin.password))
    return JsonResponse({"isShutDown": True})

def shutdown_detail_it(request, pc):
    if pc < 10:
        pc = "0" + str(pc)
    pc = "pc-it" + str(pc)

    os.system(r"net rpc -S {0} -U 'KVANTORIUM\{1}%{2}' shutdown -t 1 -f".format(pc, admin.user, admin.password))
    return JsonResponse({"isShutDown": True})


"""
HITECH KVANTUM Отключение компов.
"""

listhitech = [
    "pc-hitech01",
    "pc-hitech02",
    "pc-hitech03",
    "pc-hitech04",
    "pc-hitech05",
    "pc-hitech06",
    "pc-hitech07",
    "pc-hitech08",
    "pc-hitech09",
    "pc-hitech10",
    "pc-hitech11",
    "pc-hitech12",
    "pc-hitech13",
    "pc-hitech14",
]

def shutdown_hitech(request):
    for pc in listhitech:
        os.system(r"net rpc -S {0} -U 'KVANTORIUM\{1}%{2}' shutdown -t 1 -f".format(pc, admin.user, admin.password))
    return JsonResponse({"isShutDown": True})
