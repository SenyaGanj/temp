from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
def echo(request):

    tag = request.META.get('HTTP_X_PRINT_STATEMENT')
    params = request.GET if request.META['REQUEST_METHOD'] == "GET" else request.POST
    params_clear = {}
    for key, param in params.items():
        if param:
            params_clear[key] = param

    return render(request, 'echo.html', context={
        'values': params_clear,
        'tag': "empty" if tag is None else tag,
        'request_method': request.META['REQUEST_METHOD'].lower()
    })