# _*_ coding: utf-8 _*_
__author__ = 'wlk'
__date__ = '2018/3/26 13:40'


import xadmin

from .models import Course, Lesson, Viedo, CourseResource, BannerCourse


class LessonInline(object):
    model = Lesson
    extra = 0


# class CourseResourceInline(object):
#     model = CourseResource
#     extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                    'click_nums', 'add_time', 'get_zj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                   'image', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums', 'fav_nums']
    inlines = [LessonInline]
    list_editable = ['degree', 'desc']
    refresh_times = [3, 5]
    style_fields = {"detail": "ueditor"}
    import_excel = True
    model_icon = 'fa fa-leanpub'

    # 过滤列表中的数据
    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        # 字段联动
        obj = self.new_obj
        # 新增课程还没有保存，统计的课程数少一个
        obj.save()
        # 必须确定存在。
        if obj.course_org is not None:
            # obj实际是一个course对象
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)
# 注意：搜索字段如果有时间类型会报错


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                   'image', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums', 'fav_nums']
    inlines = [LessonInline]
    model_icon = 'fa fa-leanpub'

    # 过滤列表中的数据
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']  # course__name明确指定外键的name字段
    model_icon = 'fa fa-bandcamp'


class ViedoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    model_icon = 'fa fa-play-circle'


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']
    model_icon = 'fa fa-download'


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Viedo, ViedoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)