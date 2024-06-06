from django import template

register = template.Library()


#@register.filter
#def add1(item):
#    return item + 1


@register.inclusion_tag('my_tag/headers.html')
def banner(menu_name):
    img_list = [
        "http:///p5.qhimg.com/t01dfd5b57a47cd80a0.jpg",
        "http:///p5.qhimg.com/t01789c4234131f59e9.jpg",
        "http:///p0.qhimg.com/t01a3d15d1c3eb047aa.jpg",
    ]
    return {"img_list": img_list}
