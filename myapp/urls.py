from django.contrib import admin
from django.urls import path
from myapp.views import AddWorkerView, WorkerListView, AddOfficeView, OfficeListView, WorkerListJsonView, \
    OfficeListJsonView, WorkerCreateView, WorkerDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-worker/', AddWorkerView.as_view(), name='add_worker'),
    path('api/workers/', WorkerListJsonView.as_view(), name='worker-list-json'),
    path('api/workers/<int:id>/', WorkerDetailView.as_view(), name='worker-delete'),
    path('workers/', WorkerListView.as_view(), name='worker_list'),
    path('add-office/', AddOfficeView.as_view(), name='add_office'),
    path('api/offices/', OfficeListJsonView.as_view(), name='office-list-json'),
    path('api/offices/<int:id>/', OfficeListJsonView.as_view(), name='office-delete'),
    path('offices/', OfficeListView.as_view(), name='office_list'),
]