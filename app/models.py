from django.db import models
from mdeditor.fields import MDTextField

class article(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    excerpt = models.CharField(max_length=200,blank=True,null=True,verbose_name="描述")
    type = models.ForeignKey('category',verbose_name="文章类别")
    img = models.ImageField(upload_to='article_img/%Y/%m/%d',verbose_name='文章图片',blank=True,null=True)
    body = MDTextField()
    # body = UEditorField('文章内容',width=800,height=500,toolbars="full",imagePath="upimg/",filePath="upfile/",upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    views = models.PositiveIntegerField(verbose_name="浏览数",default=0)
    ctime = models.DateField(auto_now_add=True,verbose_name="发布时间")
    mtime = models.DateField(auto_now=True,verbose_name="修改时间")

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=64,verbose_name="分类名称")
    desc = models.CharField(max_length=128,verbose_name="类型描述")

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
    def __str__(self):
        return self.name


class banner(models.Model):
    name = models.CharField(max_length=64,default='',verbose_name='标题')
    img = models.ImageField(upload_to='banner/',verbose_name='轮播图')
    url = models.URLField(max_length=128,verbose_name='图片连接',null=True,blank=True)
    status = models.BooleanField(default=False,verbose_name='是否在使用')
    ctime = models.DateField(auto_now_add=True,verbose_name="发布时间")
    mtime = models.DateField(auto_now=True,verbose_name="修改时间")
    desc = models.TextField(verbose_name="图片描述",null=True,blank=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'
    def __str__(self):
        return self.name

