from webbrowser import get
from django.template import Library

register = Library()

@register.simple_tag
def url_replace(request, field, value):
    """
    GETパラメータの一部を置き換える。    
    """
    #Djangoのtemplate内でurlのコピーをとっている？
    url_dict = request.GET.copy()
    #新しくパラメータの指定
    url_dict[field] = str(value)
    #request.GET.copy()で取ってきたものだと長いから、.urlencodeで自分たちにも分かりやすいように変換
    return url_dict.urlencode()
