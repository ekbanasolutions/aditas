from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import account
from . import account, users, groups
# from django.conf.urls import include, url

urlpatterns = [
    url(r'^login$', account.LoginView.as_view(), name="login"),
    url(r'^signup$', account.SignUpView.as_view(), name="signup"),
    url(r'^logout$', account.LogoutView.as_view(), name="logout"),
    url(r'^add_user$', users.Add_user.as_view(), name="add_user"),
    url(r'^add_group$', groups.Add_group.as_view(), name="add_group"),
    url(r'^change_group/(?P<id>\d+)/$', groups.Change_group.as_view(), name="change_group"),
    url(r'^change_user/(?P<id>\d+)/$', users.Change_user.as_view(), name="change_user"),
    url(r'^users_index$', users.Users_index.as_view(), name="users_index"),
    url(r'^groups_index$', groups.Groups_index.as_view(), name="groups_index"),
    url(r'^users_delete$', users.Users_delete.as_view(), name="users_delete"),
    url(r'^groups_delete$', groups.Groups_delete.as_view(), name="groups_delete"),
]