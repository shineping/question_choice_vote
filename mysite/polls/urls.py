from django.urls import path

from . import views
app_name = 'polls'   #应用命名空间，防止多个APP产生同一个url，以防别名reverse反转出错。polls:url名字
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]


