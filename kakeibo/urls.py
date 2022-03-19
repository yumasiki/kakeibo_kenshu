from django.urls import path
from .views import PaymentList, IncomeList, PaymentCreate, IncomeCreate, PaymentUpdate, IncomeUpdate, PaymentDelete, IncomeDelete, MonthDashboard

app_name = "kakeibo"

urlpatterns = [
    path('', PaymentList.as_view(), name="payment_list"),
    path("income_list/", IncomeList.as_view(), name="income_list"),
    path("payment_create/", PaymentCreate.as_view(), name="payment_create"),
    path("income_create/", IncomeCreate.as_view(), name="income_create"),
    path('payment_update/<int:pk>/', PaymentUpdate.as_view(), name='payment_update'),
    path('income_update/<int:pk>/', IncomeUpdate.as_view(), name='income_update'),
    path('payment_delete/<int:pk>/', PaymentDelete.as_view(), name='payment_delete'),
    path('income_delete/<int:pk>/', IncomeDelete.as_view(), name='income_delete'),
    #月別に表示したいので、yearとmonthを指定します。
    path('month_dashboard/<int:year>/<int:month>/', MonthDashboard.as_view(), name='month_dashboard'),
]
