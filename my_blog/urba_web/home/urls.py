
from django.urls import path
from .views import *
#ипортируем кэширование
from django.views.decorators.cache import cache_page
urlpatterns = [
    #страница регистрации пользователя
    path('register/', register, name='register'),
    path('login/', User_login, name='login'),
    path('logout/', User_logout, name='logout'),
    path('send_mail/', Send_mail, name='send_mail'),


    #Домашняя страница
    #path('', Index, name='home'),
    #подключение кэша
    #path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('', HomeNews.as_view(), name='home'),
    #так подключается ссылка на категории в меню(<int:category_id>/   значит что если на вход получет число то активируется функция get_category)

    #переход на категории
    #path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),

    #Перехрд на полную новость
    #path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),

    # Добавляем новость
    path('home/add_news/', add_news, name='add_news'),
    #path('home/add_news/', CreateNews.as_view(), name='add_news'),

]