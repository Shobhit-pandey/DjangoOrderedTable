# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import simplejson as simplejson
from django.core.serializers import json
from django.shortcuts import render, redirect


# Create your views here.
from orderedtable.forms import ImportJson, ProjectTable, ProjectTable, Choice
from orderedtable.models import Project


def home(request):
    return render(request,"home.html")


def project_list(request):
    lists = Project.objects.order_by('s_no')
    return render(request, 'projects.html', {'lists': lists})


def import_json(request):
    form = ImportJson()
    if request.method == 'POST':
        form = ImportJson(request.POST, request.FILES)
        if form.is_valid():
            json = request.FILES.get('json', False)
            obj = simplejson.load(json)
            # obj = obj[13:]
            # print(obj)
            temp = []
            dictList = []
            for key, value in obj.items():
                temp = [key, value]
                dictList.append(temp)
            js = dictList[0][1]
            for i in range(len(js)):
                js_list = []
                for key, value in js[i].items():
                    temp = [key, value]
                    js_list.append(temp)
                distance = js_list[0][1]
                rate = js_list[1][1]
                project_size = js_list[2][1]
                completion_date = js_list[3][1]
                s = Project.objects.all()
                last_s_no = 0
                if s:
                    se = Project.objects.order_by('-s_no')
                    for d in se:
                        last_s_no = d.s_no
                        break
                new_s_no = last_s_no + 1
                Project.objects.create(s_no=new_s_no,distance=distance,rate=rate,completion_date=completion_date,project_size=project_size)
                # print(js_list[1][1])
            return redirect('orderedtable:project_list')
    else:
        form = ImportJson()
    return render(request, 'import_json.html', {'form': form})


def delete_table(request):
    Project.objects.all().delete()
    return redirect('orderedtable:project_list')


def sorted(request,pk):
    results = Project.objects.all()
    if pk == 'distance_a':
        results = Project.objects.order_by('distance','s_no')
    if pk == 'distance_d':
        results = Project.objects.order_by('-distance','s_no')
    if pk == 'rate_a':
        results = Project.objects.order_by('rate','s_no')
    if pk == 'rate_d':
        results = Project.objects.order_by('-rate','s_no')
    if pk == 'project_size_a':
        results = Project.objects.order_by('project_size','s_no')
    if pk == 'project_size_d':
        results = Project.objects.order_by('-project_size','s_no')
    if pk == 'completion_date_a':
        results = Project.objects.order_by('completion_date','s_no')
    if pk == 'completion_date_d':
        results = Project.objects.order_by('-completion_date','s_no')
    return render(request, 'projects.html', {"lists": results})


def multiple_sorting(request):
    if request.method == 'POST':
        form = Choice(request.POST)
        if form.is_valid():
            ch1 = request.POST['ch1']
            ch2 = request.POST['ch2']
            ch3 = request.POST['ch3']
            ch4 = request.POST['ch4']
            results = Project.objects.order_by(ch1,ch2,ch3,ch4)
            order = []
            for re in results:
                order.append(re.s_no)
            # print(order)
            k=1
            for id in results:
                id.s_no=k
                k+=1
                id.save()
            # sorted = []
            # for re in results:
            #     sorted.append(re.s_no)
            # unsorted = []
            # re = Project.objects.all()
            # for r in re:
            #     unsorted.append(r.s_no)
            #
            # for i in range(len(sorted)):
            #     Project.objects.filter(s_no=sorted[i]).update(s_no=0)
            #     Project.objects.filter(s_no=unsorted[i]).update(s_no=sorted[i])
            #     Project.objects.filter(s_no=0).update(s_no=unsorted[i])
            return render(request, 'projects.html', {"lists": results})
    else :
        form = Choice()
    return render(request, 'multiple_sorting.html', {"form": form})
