"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#------------------------------------これはルート(親)のURL設定ファイル

#親子関係を紐づけるために、親のurls.pyで子側のurls.pyの設定を読み取る
#また、全アプリケーションに共通するURLパターンがある場合は親側のurl.pyに定義していく

from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kakeibo/', include('kakeibo.urls')),      #kakeiboアプリケーションのurls.pyをinclude
]


"""
*アプリケーション配下のurls.pyをincludeするには以下の形式を用いる*

path(['URLパターン/'], include('[アプリケーション名].urls'))

"""

