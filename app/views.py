from django.shortcuts import render
from django.core.paginator import Paginator
from app import models
from app.forms import articleForm
import markdown


#博客页面和分类页面
def index(request,type_id=None):
    if type_id:
        all_article = models.article.objects.filter(type_id=type_id)
    else:
        all_article = models.article.objects.all()

    all_type = models.category.objects.all()
    all_banner = models.banner.objects.all()
    count = 0
    row_info = []
    #获取商和余数
    freque = divmod(len(all_article),3)
    for num in range(0,freque[0]):
        row_name = "line" + str(count)
        el1 = all_article[num*3]
        el2 = all_article[num*3+1]
        el3 = all_article[num*3+2]
        row_info.append([ el1, el2, el3 ])
        count += 1
    else:
        row_name = "line" + str(count)
        now_num = len(all_article) - freque[1]
        row_info.append(all_article[now_num:])

    paginator = Paginator(row_info,2)
    page = request.GET.get('page',1)
    contacts = paginator.page(page)
    return render(request,'base.html',{"data":contacts,"contacts":contacts,"all_type":all_type,"all_banner":all_banner})


#文章页面
def show_article(request,article_id):
    obj = models.article.objects.get(pk=article_id)
    all_type = models.category.objects.all()
    obj.body = markdown.markdown(obj.body,
        extensions = [
            'markdown.extensions.extra',    #缩写,表格等常用扩展
            'markdown.extensions.codehilite',   #语法高亮显示
        ]
                                 )
    form_obj = articleForm(instance=obj)
    print(form_obj)
    return render(request,"show_article.html",{"obj":form_obj,"source_obj":obj,"all_type":all_type})