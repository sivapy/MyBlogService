from jsonrpc import jsonrpc_method
from django.contrib.auth.models import User
from services.models import Blog
import json
import datetime
from _sqlite3 import IntegrityError


@jsonrpc_method('authenticateUser', authenticated=True)
def authenticateUser(request):
    return json.dumps(request.user.__dict__, default=str)

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

@jsonrpc_method('createBlog')
def createBlog(request, blogname, blogcontnet, username):
    user = User.objects.filter(username=username).first()
    blog = Blog(blog_name = blogname, blog_content = blogcontnet, date_creared = datetime.datetime.now(), blog_user = user)
    blog.save()
    return True

@jsonrpc_method('getBlogs')
def getBlogs(request, username):
    user = User.objects.filter(username=username)
    return [json.dumps(blog.__dict__, cls=DateTimeEncoder) for blog in Blog.objects.all().filter(blog_user=user)]


@jsonrpc_method('getAllPublishedBlogs')
def getAllPublishedBlogs(request):
#     return [json.dumps(blog.__dict__, default=str) for blog in Blog.objects.all()]
    return [json.dumps(blog.__dict__, cls=DateTimeEncoder) for blog in Blog.objects.all().filter(is_published=True)]

@jsonrpc_method('getAllUnPublishedBlogs')
def getAllUnPublishedBlogs(request):
    return [json.dumps(blog.__dict__, default=str) for blog in Blog.objects.all().filter(is_published=False)]

@jsonrpc_method('publishBlog')
def publishBlog(request, blogId):
    blog = Blog.objects.filter(id=blogId).first()
    blog.is_published = True
    blog.save()
    return  True

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