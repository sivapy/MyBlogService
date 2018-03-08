from jsonrpc import jsonrpc_method
from django.contrib.auth.models import User
from services.models import Blog
import json
import datetime
from _sqlite3 import IntegrityError


@jsonrpc_method('authenticateUser', authenticated=True)
def authenticateUser(request):
    return True

@jsonrpc_method('createUser')
def createUser(request,username,email,password,last_name):
    try:
        u = User.objects.create_user(username, email, password)
        u.first_name=username
        u.last_name=last_name
        u.save()
    except:
        raise IntegrityError
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