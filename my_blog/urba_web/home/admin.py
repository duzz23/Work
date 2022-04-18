from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import News_columns, Category


#редактор админки
class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News_columns
        fields = '__all__'


class News_columns_Admin(admin.ModelAdmin):
    #добавляем редактор в админку
    form = NewsAdminForm
     #какие поля показывать
    list_display = ('id', 'title','category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    #где добавить ссылку
    list_display_links = ('id', 'title')
    # Пол по которым можно осушествлять поиск
    search_fields = ('title', 'created_at')
    List_editable = ('is_published', )
    List_filter = ('is_published', 'category')
    fields = ('title','category', 'content', 'photo', 'get_photo', 'is_published', 'views','created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width = "75">')
        else:
            return 'фото не установлено'




# Register your models here.


class Category_Admin(admin.ModelAdmin):
    #какие поля показывать
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )

admin.site.register(News_columns, News_columns_Admin)
admin.site.register(Category, Category_Admin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'