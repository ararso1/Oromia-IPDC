from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/',views.register, name='register'),
    path('investor_dashboard', views.investor_dashboard, name='investor_personal_information'),
    path('request_land', views.request_land, name='requestlandpage'),
    path('investor_file_information', views.investor_file_information, name='investor_file_information'),

    path('park_admin_dashboard', views.park_admin_dashboard, name='park_admin'),
    path('manager_dashboard', views.manager_dashboard, name='oipdc_manager'),
    path('board_dashboard', views.board_dashboard, name='oipdc_board'),
    path('oiib_dashboard', views.oiib_dashboard, name='oiib'),
    path('profile/', views.investorprofilepage, name='profilepage'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutpage,name="logout"),
    path('unallowed',views.unallowedpage,name="unallowed"),
    #new added
    path('investor_profile', views.investorprofilepage, name="investor_profile"),
    path('live_camera', views.live_camera, name="live_camera"),
    path('chat',views.chatpage,name="chatpage"),
    path('privatechat/<str:pk>', views.chat, name="chat"),
    path('license_request', views.license_request, name="license_request"),
    path('all_investor', views.all_investor, name="all_investor"),
    path('view_investor_profile/<str:pk>', views.view_investor_profile, name="view_investor_profile"),
    path('proposal', views.proposal, name="proposal"),
    path('pdfviewer/<str:pk>/', views.pdfviewer, name="pdfviewer"),
    path('awesometext',views.awesome,name='awesome'),
    path('feedbacklist',views.feedbacklist , name="feedbacklist"),
    path('report/',views.reportcase,name='reportcase'),
      path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="ipdc/Investor_dashboard/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="ipdc/Investor_dashboard/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="ipdc/Investor_dashboard/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="ipdc/Investor_dashboard/password_reset_done.html"), 
        name="password_reset_complete"),

    
]

