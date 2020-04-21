# echarts_dj
A django project demo which using  django2.2, mysql, echarts

项目描述: django项目关联 echarts, 连接mysql数据库，前端通过ajax请求后台, 动态展示数据库中的数据
下载echarts组件: https://echarts.baidu.com/download.html
Django环境搭建:
 pycharm + python3.6 + django2.2 
 pip install mysqlclient


line_demo.html
function line_charts_lc(){
    $.ajax({
        url: '/linecharts/', #请求后台view.py中的方法
        type: 'post',
        dataType: "json",
        data: {},
        success: function(response){
            //line_option.legend.data = response.dates;
            line_option.xAxis.data = response.xtimes;
            //line_option.series[0].name = response.dates[0];
            line_option.series[0].data = response.values;
            line_chart.setOption(line_option);
            line_chart.hideLoading();
        }
    })
}

settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abc', # database name
        'USER': 'root',
        'PASSWORD': 'admin',
    }
}

models.py
class Linecharts(models.Model):
    linetime = models.DateTimeField(blank=True, null=True)
    linevalue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linecharts'

view.py
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
