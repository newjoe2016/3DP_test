from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from Printapp.models import  UserProfile,StlFile,Model_project,Printer
# Register your models here.
class ProfileInline(admin.StackedInline):
	model = UserProfile
	fk_name='user'  
	max_num=1 

class UserProfileAdmin(UserAdmin):
	inlines = [ProfileInline,]

class StlAdmin(admin.ModelAdmin):
	list_display = ('stl_owner','stl_name','stl_date')

class ModelAdmin(admin.ModelAdmin):
	list_display = ('model_owner','model_name','model_price','model_date')

admin.site.unregister(User) 
admin.site.register(User, UserProfileAdmin)


admin.site.register(StlFile,StlAdmin)
admin.site.register(Model_project,ModelAdmin)
admin.site.register(Printer)