# フォームの作成

from django import forms
from .models import Kakeibo

#Django標準のformsモジュール内に定義されているModelFormクラスを継承して家計簿データ登録用のフォームクラス(KakeiboForm)を定義
class KakeiboForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """
    class Meta:
        model = Kakeibo
        fields =['date', 'category', 'money', 'memo'] 