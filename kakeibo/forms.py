from django import forms
from .models import PaymentCategory, Payment, Income
from django.utils import timezone


class PaymentSearchForm(forms.Form):
    """支出検索フォーム"""

    # 年の選択肢を動的に作る
    start_year = 2022  # 家計簿の登録を始めた年
    end_year = timezone.now().year + 1  # 現在の年+1年
    #(year, f'{year}年')は、全て、choicesに入れ込むために作成している。第一引数はDBに認識させるため、第二引数は、表示させるためのデータを入れ込む。
    years = [(year, f'{year}年')
             for year in reversed(range(start_year, end_year + 1))]
    years.insert(0, (0, ''))  # 空白の選択を追加
    YEAR_CHOICES = tuple(years)

    # 月の選択肢を動的に作る。
    months = [(month, f'{month}月') for month in range(1, 13)]
    months.insert(0, (0, ''))
    MONTH_CHOICES = tuple(months)

    # 年の選択
    """・requiredはフォームでの入力を必須とするか否か?を True or False で答えさせる。
       ・widgetはhtmlでの表記方法を示すもの
       ・attrsはレンダリングされたウィジェットに設定するHTML属性を含む辞書
       ・forms.Selectはプルダウンリストでリストの一覧を表示する。"""
    year = forms.ChoiceField(label='年での絞り込み',
                             required=False,
                             choices=YEAR_CHOICES,
                             widget=forms.Select(attrs={'class': 'form'}))

    # 月の選択
    month = forms.ChoiceField(label='月での絞り込み',
                              required=False,
                              choices=MONTH_CHOICES,
                              widget=forms.Select(attrs={'class': 'form'}))

    # 〇〇円以上
    greater_than = forms.IntegerField(
        label='Greater Than',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form',
            'autocomplete': 'off',
            'placeholder': '〇〇円以上'
        }))

    # 〇〇円以下
    less_than = forms.IntegerField(
        label='Less Than',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form',
            'autocomplete': 'off',
            'placeholder': '〇〇円以下'
        }))

    # キーワード
    key_word = forms.CharField(
        label='検索キーワード',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form',
            'autocomplete': 'off',
            'placeholder': 'キーワード',
        }))

    # カテゴリー検索
    """
    queryset=PaymentCategory.objects.order_by('name')は
    PaymentCategoryモデルのnameフィールドを昇順にした値の一覧表を取得。
    widget=forms.Select(attrs={'class': 'form'}))でその一覧データからプルダウンリストで選択させる。
    """
    category = forms.ModelChoiceField(
        label='カテゴリでの絞り込み',
        required=False,
        queryset=PaymentCategory.objects.order_by('name'),
        #forms.Selectは、プルダウンリスト
        widget=forms.Select(attrs={'class': 'form'}))

class IncomeSearchForm(forms.Form):
    """支出検索フォーム"""

    # 年の選択肢を動的に作る
    start_year = 2022  # 家計簿の登録を始めた年
    end_year = timezone.now().year + 1  # 現在の年+1年
    #(year, f'{year}年')は、全て、choicesに入れ込むために作成している。第一引数はDBに認識させるため、第二引数は、表示させるためのデータを入れ込む。
    years = [(year, f'{year}年')
             for year in reversed(range(start_year, end_year + 1))]
    years.insert(0, (0, ''))  # 空白の選択を追加
    YEAR_CHOICES = tuple(years)

    # 月の選択肢を動的に作る。
    months = [(month, f'{month}月') for month in range(1, 13)]
    months.insert(0, (0, ''))
    MONTH_CHOICES = tuple(months)

    # 年の選択
    """・requiredはフォームでの入力を必須とするか否か?を True or False で答えさせる。
       ・widgetはhtmlでの表記方法を示すもの
       ・attrsはレンダリングされたウィジェットに設定するHTML属性を含む辞書
       ・forms.Selectはプルダウンリストでリストの一覧を表示する。"""
    year = forms.ChoiceField(label='年での絞り込み',
                             required=False,
                             choices=YEAR_CHOICES,
                             widget=forms.Select(attrs={'class': 'form'}))

    # 月の選択
    month = forms.ChoiceField(label='月での絞り込み',
                              required=False,
                              choices=MONTH_CHOICES,
                              widget=forms.Select(attrs={'class': 'form'}))

class PaymentCreateForm(forms.ModelForm):
    """支出登録フォーム"""

    class Meta:
        model = Payment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form'
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['autocomplete'] = 'off'


class IncomeCreateForm(forms.ModelForm):
    """収入登録フォーム"""

    class Meta:
        model = Income
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            #classは、cssやJavascriptで指定する際に用いられる。
            field.widget.attrs['class'] = 'form'
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['autocomplete'] = 'off'
