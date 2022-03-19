from django.utils import timezone

def common(request):
    """家計のアプリの共通コンテキスト"""
    now = timezone.now()

    return {"now_year": now.year,
            "now_month": now.month}
