# _*_ coding: utf-8 _*_
__author__ = 'wlk'
__date__ = '2018/3/26 14:59'


import xadmin
from .models import UserAsk, CourseComments, CourseFavorite, UserCourse,UserMessage


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    model_icon = 'fa fa-building'


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']
    model_icon = 'fa fa-envelope'


class CourseFavoriteAdmin(object):
    list_display = ['user', 'course', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'course', 'fav_id', 'fav_type']
    list_filter = ['user', 'course', 'fav_id', 'fav_type', 'add_time']
    model_icon = 'fa fa-heart-o'


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
    model_icon = 'fa fa-file-word-o'


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    model_icon = 'fa fa-paper-plane-o'


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(CourseFavorite, CourseFavoriteAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)