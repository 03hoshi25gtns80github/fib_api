from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

def fibonacci_number(request):
    # クエリパラメータnを取得
    n = request.GET.get('n')
    # nが「存在しない, 空文字列, 整数ではない」場合
    if n is None or n == '' or not n.isdigit():
        return JsonResponse({'status': 400, 'message': 'Bad request.'}, status=400)
    
    # nを整数に変換
    n = int(n)
    # nが「負の数, 非常に大きな数」の場合
    if n < 0 or n > 20000:  # 出力が4000桁を上限としています
        return JsonResponse({'status': 400, 'message': 'Bad request.'}, status=400)
    
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
    
    result = fibonacci(n)
    return JsonResponse({'result': result})