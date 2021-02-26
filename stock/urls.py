from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('deletestock/<stock_symbol>', views.delete_stock, name='delete_stock'),

]
