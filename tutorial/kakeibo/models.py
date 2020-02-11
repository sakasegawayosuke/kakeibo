from django.db import models
from datetime import datetime

# Create your models here.

#--------Pythonのクラスとしてtableを定義-----------
#クラスを定義する際に、Dajgo標準のmodelsクラスを継承

#----------------------------------------------------家計簿のカテゴリテーブルを作る
class Category(models.Model):
    class Meta:
        #テーブル名の指定
        db_table = "category"

        #テーブルの表示を日本語に変更
        verbose_name = "カテゴリ"
        verbose_name_plural = "カテゴリ"

    #カラム名の定義
    category_name = models.CharField(max_length=255, unique=True)

    #テーブル項目のフォーマット
    """
    <項目名> = models.<データ型>(フィールドオプション)

    #max_length : 最大サイズ
    #unique : 重複を許可するか      (unique = True　で重複を許可しない)

    """

    #adminサイトで表示される文字列を定義する
    def __str__(self):
        return self.category_name


#---------------------------------------------------------------家計簿テーブルを作る
class Kakeibo(models.Model):
    class Meta:
        #テーブル名
        db_table = "kakeibo"

        #テーブルの表示を日本語に変更
        verbose_name = "家計簿"
        verbose_name_plural = "家計簿"

    #カラムの定義
    date = models.DateTimeField(verbose_name="日付", default=datetime.now)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name="カテゴリ")
    money = models.IntegerField(verbose_name="金額", help_text="単位は日本円")
    memo = models.CharField(verbose_name="メモ", max_length=500)

    #外部キーを設定する場合
    """
    [項目名] = models.ForeignKey([参照先のテーブルクラス名], on_delete=[オプション],[その他のフィールドオプション])

    on_delete : 参照するオブジェクトが削除された時に、それと紐づけられたオブジェクトも一緒に削除するかどうかを設定
    (models.PROTECT　保護する(参照されていたら削除されない))

    """

    #adminサイトで表示される文字列を定義する
    def __str__(self):
        return self.memo


