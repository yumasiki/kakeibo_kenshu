from django.db import models

# Create your models here.


#カテゴリ名を保存するためのモデル
class PaymentCategory(models.Model):
    name = models.CharField("カテゴリ名", max_length=32)

    #カテゴリ名を入力されたものをそのまま返すようにしている。
    def __str__(self):
        return self.name


class Payment(models.Model):
    date = models.DateField("日付")
    price = models.IntegerField("金額")
    """
    on_delete=models.PROTECT	は結びついている子データがある場合は親データを削除できない
    
    ForeignKeyは多対1の多の子側につけられるもの。
    ForeignKey(紐づけるモデル名, on_delete=親フィールドが削除されたときの動作, **options)

    下記の例では、
    PaymentはPaymentCategoryの子側としてモデル（テーブル）同士の関係性を結びつけている。
    """
    """verbose_name='○○'は
     verbose_nameの扱い方について
モデルにおいて指定する場所でそれぞれ変更するものが違う。
・メタデータ内での指定:モデル名の変更
・フィールド内での指定:フィールド名の変更

詳しくは以下参照
https://office54.net/python/django/model-verbose-name
    """
    category = models.ForeignKey(PaymentCategory,
                                 on_delete=models.PROTECT,
                                 verbose_name="カテゴリ")
    description = models.TextField('摘要', null=True, blank=True)


#以下、Incomeにおいても同じコード。
class IncomeCategory(models.Model):
    name = models.CharField('カテゴリ名', max_length=32)

    def __str__(self):
        return self.name


class Income(models.Model):
    date = models.DateField('日付')
    price = models.IntegerField('金額')
    category = models.ForeignKey(IncomeCategory,
                                 on_delete=models.PROTECT,
                                 verbose_name='カテゴリ')
    description = models.TextField('摘要', null=True, blank=True)
