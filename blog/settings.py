import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'z^^=ci!e(kshm9(qhvg!!usk&sb75v9y_yrgez^@o5os2*sc##'

DEBUG = True

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'DjangoUeditor',
    'mdeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'



DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'rootroot',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static')

# MDEDITOR_CONFIGS = {
#     'width': '90%',  # 自定义编辑框宽度
#     'heigth': 500,   # 自定义编辑框高度
#     'toolbar': ["undo", "redo", "|",
#                 "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
#                 "h1", "h2", "h3", "h5", "h6", "|",
#                 "list-ul", "list-ol", "hr", "|",
#                 "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
#                 "emoji", "html-entities", "pagebreak", "goto-line", "|",
#                 "help", "info",
#                 "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
#     'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
#     'image_floder': 'editor',  # 图片保存文件夹名称
#     'theme': 'dark',  # 编辑框主题 ，dark / default
#     'preview_theme': 'dark',  # 预览区域主题， dark / default
#     'editor_theme': 'pastel-on-dark',  # edit区域主题，pastel-on-dark / default
#     'toolbar_autofixed': True,  # 工具栏是否吸顶
#     'search_replace': True,  # 是否开启查找替换
#     'emoji': True,  # 是否开启表情功能
#     'tex': True,  # 是否开启 tex 图表功能
#     'flow_chart': True,  # 是否开启流程图功能
#     'sequence': True  # 是否开启序列图功能
# }
