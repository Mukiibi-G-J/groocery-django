from http.client import HTTPResponse
from unicodedata import category
from django.contrib import admin
from django import forms
from .models import Category
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse

class CategoryAdminCsv(forms.Form):
    csv_upload = forms.FileField()



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['category_name','category_image']


    def upload_csv(self, request):
        form = CategoryAdminCsv()


        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, "This is a wrong file upload it must be  .csv file")
                return HttpResponseRedirect(request.path_info)
            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split("\n")
            total_count = []

            for count, x in enumerate(csv_data):
                fields = x.split(',')
                total_count.append(count)
                print(total_count)

                if len(fields[0])> 0:
                    created = Category.objects.update_or_create(
                    category_name=str(fields[0]))
            messages.success(request, f"{len(total_count)} categories have been added succefull")  
            url = reverse('admin:index')
            return HttpResponseRedirect(url)
        context ={"form":form}
        return render(request, 'admin/csv_upload.html',context)
      
    #registeting  a a url  to admin site    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv)]
        return new_urls + urls