#アプリケーション(子側)のurls.pyの設定
from django.urls import path

from . import views     #views.pyとurls.pyは同じディレクトリに存在しているため「from .」でimportできる

#名前空間を定義
#名前空間を利用すると、テンプレート(html)から{% url'[名前空間名] : [URLパターン名称]' %}というフォーマットで逆引きでURLパターンを呼び出すことができる

app_name = 'kakeibo'

urlpatterns = [
    path('kakeibo_list/', views.KakeiboListView.as_view(), name='kakeibo_list'),
    path('kakeibo_create/', views.KakeiboCreateView.as_view(), name='kakeibo_create'),    #新規登録画面用のURLパターンを設定
    path('create_done/', views.create_done, name='create_done'),        #新規登録が正常に終了した時に、reverse_lazyメソッドから呼ばれるURLパターンを指定

    path('update/<int:pk>/', views.KakeiboUpdateView.as_view(), name='kakeibo_update'),     #更新画面用のURLパターンを指定
    #↑↑家計簿データ一覧表示画面(kakeibo_list.html)から逆引きでURLパターン「kakeibo_update」を引数(家計簿データレコードのPKキー)付きで呼び出した際に、
    # URLパターンの<int:pk>の部分に家計簿データレコードのPKの値がリセットされる。
    path('update_done/', views.update_done, name='update_done'),        #更新処理が正常に終了した時に、reverse_lazyメソッドから呼ばれるURLパターンを指定

    path('delete/<int:pk>/', views.KakeiboDeleteView.as_view(), name='kakeibo_delete'),     #削除画面用のURLパターンを指定。更新の時と形は同じ
    path('delete_done/', views.delete_done, name='delete_done'),        #削除が正常に終了した時に、reverse_lazyメソッドから呼ばれるURLパターンを指定

    path('circle/', views.show_circle_grahp, name='kakeibo_circle'),    #円グラフのURLパターンを指定

]



"""
*urlパターンの設定*

path('URLパターン', '呼び出すview関数', 'URLパターンの名称')

"""