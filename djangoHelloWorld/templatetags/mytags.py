from django import template
# 导入mark_safe，用于定义语义化标签
from django.utils.safestring import mark_safe

# reigster名字固定
register = template.Library()

# 修改 settings.py 中的 TEMPLATES 的 OPTIONs，添加 libraries 配置

# 利用装饰器 @register.filter 自定义过滤器
@register.filter
def my_filter(v1, v2):
    return v1 + v2

# 利用装饰器 @register.simple_tag 自定义标签
@register.simple_tag
def my_tag(v1, v2):
    return v1 * v2

@register.simple_tag
def my_html(v1):
    temp_html = '<p style="color: red">%s</p>' %(v1)
    return mark_safe(temp_html)
