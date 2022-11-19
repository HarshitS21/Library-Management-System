from django.contrib import admin
from App_1.models import Contact,Book,User

admin.site.register(Contact), #Registers your model here.After doing this goto the apps.py file and copy the name of your app and paste it into settings.py in installed apps section with App_1.apps.Copied_name.
admin.site.register(Book),
admin.site.register(User)
# Register your models here.
