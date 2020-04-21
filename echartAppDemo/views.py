from echartAppDemo.models import Linecharts
import json
import datetime
from django.shortcuts import render, HttpResponse
# Create your views here.


def line_chars(request):
    if request.method == 'POST':
        now = datetime.datetime.now()
        dates = [now.strftime('%Y-%m-%d')]
        print(f" dates  {dates}")
        lines = Linecharts.objects.all()
        xtimes = []
        values = []
        for line in lines:
            lxtime = line.linetime.strftime('%Y-%m-%d')
            lvalue = line.linevalue
            xtimes.append(str(lxtime))
            values.append(lvalue)

        result = json.dumps({'dates': dates, 'xtimes': xtimes, 'values': values})
        return HttpResponse(result, content_type='application/json')

    return render(request, 'line_demo.html', locals())