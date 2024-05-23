from django.views import View
from rest_framework import generics, views, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
import json

from .models import Office, Worker
from .serializers import OfficeSerializer, WorkerSerializer
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class WorkerCreateView(generics.CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerListView(TemplateView):
    template_name = 'main/worker_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workers'] = Worker.objects.all()
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        worker_id = kwargs.get('pk')
        worker = get_object_or_404(Worker, id=worker_id)
        worker.delete()
        return JsonResponse({'status': 'success'})

class WorkerListJsonView(View):
    def get(self, request, *args, **kwargs):
        workers = Worker.objects.all().values('id', 'first_name', 'last_name', 'birth_date', 'hire_date', 'profession')
        workers_list = list(workers)
        return JsonResponse(workers_list, safe=False)


class AddOfficeView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer



class AddWorkerView(View):
    @method_decorator(csrf_exempt)
    def get(self, request):
        return render(request, 'main/add_worker.html')

    @method_decorator(csrf_exempt)
    def post(self, request):
        try:
            data = json.loads(request.body)
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            birth_date = data.get('birth_date')
            hire_date = data.get('hire_date')
            profession = data.get('profession')
            offices_ids = data.get('offices', [])
            offices = Office.objects.filter(id__in=offices_ids)

            worker = Worker.objects.create(
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                hire_date=hire_date,
                profession=profession
            )
            worker.offices.set(offices)
            worker.save()

            return JsonResponse({'status': 'success', 'worker_id': worker.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
class OfficeListJsonView(View):
    def get(self, request, *args, **kwargs):
        offices = Office.objects.all().values('id', 'name', 'location')
        offices_list = list(offices)
        return JsonResponse(offices_list, safe=False)

    def delete(self, request, *args, **kwargs):
        office_id = kwargs.get('id')
        office = get_object_or_404(Office, id=office_id)
        office.delete()
        return JsonResponse({'status': 'success'}, status=204)


class OfficeListView(TemplateView):
    template_name = 'main/office_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offices'] = Office.objects.all()
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class WorkerDetailView(View):
    def delete(self, request, *args, **kwargs):
        worker_id = kwargs.get('id')
        worker = get_object_or_404(Worker, id=worker_id)
        worker.delete()
        return JsonResponse({'status': 'success'}, status=204)