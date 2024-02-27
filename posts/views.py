from django.shortcuts import render

def create_sample_instances(request):
    return render(request, 'create_sample_instances.html')