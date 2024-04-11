from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("our_services/",views.our_services,name="our_services"),
    path("ai_robot/",views.ai_robot,name="ai_robot"),
    path("profit_details/",views.profit_details,name="profit_details"),
    path("contact/",views.contact,name="contact"),
    # path('ai_robot/', views.ProfitView.as_view(), name='ai_robot'),
    path('ai_robot/profits/create/', views.CreateProfit.as_view(), name='crud_ajax_create'),
    path('ai_robot/profits/delete/', views.DeleteProfit.as_view(), name='crud_ajax_delete'),
    path('ai_robot/profits/update/', views.UpdateProfit.as_view(), name='crud_ajax_update'),
    # path("edit",views.edit,name="edit"),
]
