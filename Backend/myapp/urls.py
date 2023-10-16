from django.contrib import admin
from django.urls import path
from myapp import views
from .views import TotalResultsView
from .views import AverageSalaryView
from .views import Mediansalary
from .views import threeforth
from .views import oneforth

urlpatterns = [
    path("", views.index, name='myapp'),
    path('insert/', views.import_data_from_csv, name='insert_data'),
    path('total-results/', TotalResultsView.as_view(), name='total-results'),
    path('average-salary/', AverageSalaryView.as_view(), name='average-salary'),
    path('median/', Mediansalary.as_view(), name='median-salary'),
    path('oneforth/', oneforth.as_view(), name='one_forth-salary'),
    path('threeforth/', threeforth.as_view(), name='three_forth-salary'),
]




