from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate
from .forms import CandidateModelForm
from datetime import datetime

# Create your views here.

def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request,'index.html',context)

def candidate_detail(request, candidate_id):
    context = {}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'detail.html', context)

def candidate_create(request):
    context = {}
    context['candidateform'] = CandidateModelForm(initial={'birthday' : datetime.now()})
    if request.method == 'POST':
        candidateform = CandidateModelForm(request.POST)
        if candidateform.is_valid():
            candidateform.save()
            return redirect('')
        else:
            context['candidateform'] = candidateform
            render(request, 'Ccreate.html', context)
    else:
        return render(request, 'Ccreate.html', context)

def candidate_update(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    if request.method == 'POST':
        candidateform = CandidateModelForm(request.POST, instance=candidate)
        if candidateform.is_valid():
            candidateform.save()
            return redirect('<int:candidate_id>/')
            return HttpResponse('Question updated')
        else:
            context['candidateform'] = candidateform
            render(request, 'update.html', context)
    else:
        context['candidateform'] = CandidateModelForm(instance=candidate)
    return render(request, 'update.html', context)

def positioncreate(request):
    context = {}
    context['positionform'] = PositionModelForm()
    if request.method == 'POST':
        positionform = PositionModelForm(request.POST)
        if positionform.is_valid():
            positionform.save()
            return redirect('')
        else:
            context['positionform'] = positionform
            render(request, 'Pcreate.html', context)
    else:
        return render(request, 'Pcreate.html', context)

def vote(request):
    candidate = Candidate.objects.get(id=candidate_id)
    candidate.<related_name>.all().count()
    return redirect('')
