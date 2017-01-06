from django.http import HttpResponse
import datetime
from django.template import  Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response


def hello(request):
    return HttpResponse("hello world")

def index(request):
#    wl = get_template('index.html')
#    html = wl.render(Context({'welcome':"welcome ! this a test page!"}))
#    return HttpResponse(html)


    return render_to_response('index.html', {'welcome': "welcome ,test pages"})

def cur_time(request):
    now = datetime.datetime.now()
#    html = "<html><body><h1>It is now %s.</body></html>" %now
    t=get_template('hello.html')
    html = t.render(Context({'c':now}))
    return HttpResponse(html)


def cur_hour(request, offset):
#    try:
#        offset = int(offset)    #
#    except ValueError:
#        raise Http404

    dt = datetime.datetime.now() + datetime.timedelta(hours=int(offset))
#   html = "<html><body><h1>In %s hour(s),It will be   %s.</body></html>" % (offset, dt)
#    return HttpResponse(html)
#   return  render_to_response('time.html',({'offset':offset} , {'time':dt}))

#    t = get_template('time.html')
#    html = t.render(Context({'hours': offset , 'time':dt }))
#    return HttpResponse(html)

    return  render_to_response('time.html', {'hours':offset , 'time': dt})