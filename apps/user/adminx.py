# _*_ coding: utf-8 _*_

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, Banner, UserProfile
from xadmin.layout import Main, Row, Side, Fieldset
from django.utils.translation import ugettext as _


# class UserProfileAdmin(UserAdmin)
#     pass

class BaseSetting(object):          # 主题管理器
    enable_themes = True             # 使用主题
    use_bootswatch = True


class GlobalSetting(object):           # 头部系统名称和底部版权管理器
    site_title = '合师教育管理系统'        # 头部系统名称
    site_footer = '@--wlk版权所有'      # 底部版权
    menu_style = 'accordion'          # 底部版权


class UserProfileAdmin(UserAdmin):
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active',  'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


class EmailVerifyRecordAdmin(object):  # 继承顶层的object类
    list_display = ['code', 'email', 'send_type', 'send_time']  # 展示
    search_fields = ['code', 'email', 'send_type']  # search_fields字段名称不能错，否则无法显示搜索框
    list_filter = ['code', 'email', 'send_type', 'send_time']  # 过滤器
    model_icon = 'fa fa-envelope-open-o'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    model_icon = 'fa fa-quora'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)       # 将主题管理器绑定views.BaseAdminView注册
xadmin.site.register(views.CommAdminView, GlobalSetting)    # 头部系统和底部版权管理器绑定views。CommAdminView注册