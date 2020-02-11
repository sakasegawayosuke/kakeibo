from django.shortcuts import render
from .forms import KakeiboForm
from django.urls import reverse_lazy        #ページ遷移用メソッド

# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category, Kakeibo

#一覧表示用のDjango標準ビュー(ListView)を継承して一覧表示用のクラスを定義
class KakeiboListView(ListView):
    #利用するモデルを指定
    model = Kakeibo
    
    #データを渡すテンプレートファイルを指定
    template_name = 'kakeibo/kakeibo_list.html'

    #家計簿テーブルの全データを取得するメソッドを定義
    #テンプレート側には「object_list」という名前でオブジェクトが渡される

    def queryset(self):
        return Kakeibo.objects.all()

    """
    Djangoのモデルマネージャーを利用したSQL文を使用しないデータ取得方法

    *テーブルデータを全件取得*
    [modelクラス名].objects.all()

    *特定の条件に一致する複数レコードを取得*
    [modelクラス名].objects.filter([カラム名] = '値')

    """


#新規データ登録用に用意されているCreateView汎用ビュークラスを継承してKakeiboCreateViewクラスを定義
class KakeiboCreateView(CreateView):

    #利用するモデルを指定
    model = Kakeibo
    #利用するフォームクラス名を指定
    form_class = KakeiboForm
    #登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('kakeibo:create_done')      #reverse_lazyメソッドを使って遷移先のurlを指定

def create_done(request):
    #登録処理が正常に終了した場合に呼ばれるテンプレートを指定
    return render(request, 'kakeibo/create_done.html')

#----------------------------------------------------------------------------------------------

#データの更新用に用意されているUpdateView汎用ビュークラスを継承してKakeiboUpdateViewを定義
class KakeiboUpdateView(UpdateView):

    #利用するモデルを指定
    model = Kakeibo
    #利用するフォームクラス名を指定
    form_class = KakeiboForm
    #更新処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('kakeibo:update_done')

def update_done(request):
    #更新処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'kakeibo/update_done.html')

#----------------------------------------------------------------------------------------------

#データ削除用に用意されているDeleteView汎用ビュークラスを継承してKakeiboDeleteViewを定義
class KakeiboDeleteView(DeleteView):

    #利用するモデルを指定
    model = Kakeibo
    #削除処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('kakeibo:delete_done')

def delete_done(request):
    #削除処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'kakeibo/delete_done.html')
