from django import template
from home.models import Category
from django.db.models import Count, F
from django.core.cache import cache

register = template.Library()


@register.simple_tag(name='get_cat')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('home/list_cat.html')
def show_categories(arg1='Helo', arg2= 'Word'):
    #кэширование если его нет тогда берем из базы даннх
    #categories = cache.get('categories')
    #if not categories:
    #categories = Category.objects.all()
   #убираем отображение пустых категорий
    categories = Category.objects.annotate(cnt=Count('news_columns', filter=F('news_columns__is_published'))).filter(cnt__gt=0)

        #cache.set('categories', categories, 30)
    return {"categories": categories, "arg1": arg1, "arg2": arg2}

