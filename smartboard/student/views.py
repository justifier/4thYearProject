from django.http import HttpResponse
from django.contrib.auth.models import User


def create_user(request):
    user = User.objects.create_user(
        username='nancy',
        password='opensesame',
        email='nancy@nancy.com'
    )
    user.save()
    email = User.objects.get(username='nancy').email
    output = '''
    <html>
      <head>
        <title>
          Connecting to the model
        </title>
      </head>
      <body>
        <h1>
          Connecting to the model
        </h1>
        The new user's email: %s
      </body>
    </html>''' % (
        email
    )
    return HttpResponse(output)
