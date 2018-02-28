from jsonrpc import jsonrpc_method
from django.contrib.auth.models import User
from services.models import Blog
import json
import datetime

@jsonrpc_method('authenticateUser', authenticated=True)
def authenticateUser(request):
    return True

@jsonrpc_method('createUser')
def createUser(request, username, password):
    u = User.objects.create_user(username, 'internal@app.net', password)
    u.save()
    return True

@jsonrpc_method('getBlogs')
def getBlogs(request):
    return [json.dumps(task.__dict__, cls=DateTimeEncoder) for task in Blog.objects.all()]


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return obj.__dict__