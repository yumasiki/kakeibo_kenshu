from django.contrib import admin
from .models import Payment, Income, PaymentCategory, IncomeCategory

#csvファイルなどのインポートエクスポートをするための仕組み
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


#インポートエクスポートリソースの作成。
class PaymentResource(resources.ModelResource):

    class Meta:
        model = Payment


#ImportExportModelAdminのサブクラスを作成により、adminで操作できるようにする。Paymentのオプション機能のようなもの。
class PaymentAdmin(ImportExportModelAdmin):
    #PaymentResource（Paymentと同じ扱い）のdescriptionフィールドの検索
    search_fields = ('description', )
    #PaymentResource（Paymentと同じ扱い）の以下のフィールドごとに縦に一覧表示する。
    list_display = ['date', 'category', 'price', 'description']
    #PaymentResource（Paymentと同じ扱い）のcategoryフィールドのフィルター機能を持った一覧表
    list_filter = ('category', )
    #PaymentResource（Paymentと同じ扱い）のdateフィールドの降順表示機能
    ordering = ('-date', )
    #リソースクラスの参照先として、作成されたリソースを配置
    resource_class = PaymentResource


class PaymentCategoryResource(resources.ModelResource):

    class Meta:
        model = PaymentCategory


class PaymentCategoryAdmin(ImportExportModelAdmin):
    resource_class = PaymentCategoryResource


class IncomeResource(resources.ModelResource):

    class Meta:
        model = Income


class IncomeAdmin(ImportExportModelAdmin):
    search_fields = ('description', )
    list_display = ['date', 'category', 'price', 'description']
    list_filter = ('category', )
    ordering = ('-date', )

    resource_class = IncomeResource


class IncomeCategoryResource(resources.ModelResource):

    class Meta:
        model = IncomeCategory


class IncomeCategoryAdmin(ImportExportModelAdmin):
    resource_class = IncomeCategoryResource


#モデルを admin.py に登録して操作できるようにする。
#第1引数に対して、第２引数のオプションが適用されるイメージ
admin.site.register(PaymentCategory, PaymentCategoryAdmin)
admin.site.register(IncomeCategory, IncomeCategoryAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Income, IncomeAdmin)
