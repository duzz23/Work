import os

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.core.paginator import Paginator
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForms
from .models import News_columns, Category
from django.urls import reverse_lazy
#если надо страницу закрыть для не авторезированых пользовотелей
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
import logging,traceback

logger = logging.getLogger('django')



#Отправка писем email
def Send_mail(request):
    if request.method == "POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], settings.EMAIL_HOST_USER, ['duzz@mail.ru'], auth_user= settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD)
            if mail:
                messages.success(request, 'Send email')
                return redirect('send_mail')
            else:
               messages.error(request, 'Error Send')
        else:
            messages.error(request, 'Error reg')
    else:
        form = ContactForms()
    return render(request, 'home/send_mail.html', {"form": form})


#регистрация пользователя и сохранение данных
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            for message in form.error_messages:
                messages.error(request, message)
    else:
        form = UserRegisterForm()
    return render(request, 'home/register.html', {"form": form})

def User_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'home/login.html', {"form": form})

def User_logout(request):
    logout(request)
    return redirect('login')


# заменем этим классом функцию index
#Задача класса вернуть список
class HomeNews(MyMixin, ListView):
    model = News_columns
    template_name = 'home/news_columns_list.html'
    context_object_name = 'news'
    mixin_prop = 'hello word'
    #Количество новостных блоков на одно странице
    paginate_by = 2
    # Титульный лист подписываем в ручную
    #extra_context = {'title':  'Главная страница'}
    # Титульный лист проставляется автоматически
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.get_upper делвет написание титула большими буквами
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

#отоброжение только тех новостей у которыъ стоит галочка
    def get_queryset(self):
        #return News_columns.objects.filter(is_published=True)
        #метод позволяет снизить количество запросов к БД (если ForeignKey)
        return News_columns.objects.filter(is_published=True).select_related('category')
#заменем этим классом функцию category
#Создаем переход по гурппам в меню
class NewsByCategory(MyMixin, ListView):
    model = News_columns
    template_name = 'home/news_columns_list.html'
    context_object_name = 'news'
    #Неразрешать показ страниц которых нет
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return News_columns.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')
    #Отображение название title в шапке вкланки страници
    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #self.get_upper делвет написание титула большими буквами
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))

        return context

#Прописывая Класс, для ссылку перехпда на полную новость
class ViewNews(DetailView):
    model = News_columns
    context_object_name = 'news_item'
    #template_name = 'home/news_columns_detail.html' если друго шаблон тут можно указать

#Добавление новости
class CreateNews(LoginRequiredMixin, CreateView):
    from_class = NewsForm
    template_name = 'home/add_news.html'
    login_url = '/admin/'

    #success_url = reverse_lazy('home')


   






#def index(request):
#    context = {
#       'news': news,
#        'title': 'Список новостей',
#    }
#    return render(request, template_name='home/index.html', context=context)

#Создаем переход по гурппам в меню
#def get_category(request, category_id):
#    category = Category.objects.get(pk=category_id)
#    return render(request, 'home/category.html', {'news':news, 'category':category})

#Прописывая ссылку перехпда на полную новость
#def view_news(request, news_id):
#    #news_item = News_columns.objects.get(pk=news_id)
#    news_item = get_object_or_404(News_columns, pk=news_id)
#    return  render(request, 'home/view_news.html', {"news_item":news_item})

#Функция "Добавления новости"
#откуда у меня NewsfForms?????
def add_news(request):
   if request.method == 'POST':
       form = NewsForm(request.POST)
       if form.is_valid():
           #print(form.cleaned_data)
           #сахраняем добавленную новолть
           #news = News_columns.objects.create(**form.cleaned_data)
           news = form.save()
           return redirect(news)
   else:
       form = NewsForm()
   return render(request, 'home/add_news.html', {'form':form})
