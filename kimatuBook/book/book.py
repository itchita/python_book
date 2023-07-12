from flask import Blueprint, render_template, request
import db

# Blueprint インスタンスを作成
# 第1引数は Blueprint の名前
# 第2引数はモジュール名(__name__を指定すればOK)
# 第3引数は Blueprint の URL プレフィックス
book_bp = Blueprint('book', __name__, url_prefix='/book')

# Blueprint インスタンスにルーティングを設定する。
# この場合は book_bp の url_prefix が /book なので
# このメソッドの URL は /book/list となります。
@book_bp.route('/list')
def book_list():
    book_list = [
        ('よく分かるPython', '佐々木 磨生', 'MCL出版', 200),
        ('LinuC 詳解', '細川 潤哉', 'MCL出版', 400),
        ('Servlet 入門', '高橋 洋平', 'ジョビ出版', 250),
        ('Flask 入門', '高橋 洋平', 'ジョビ出版', 150),
        ('よく分かるUML', '細川 潤哉', 'MCL出版', 220),
        ('Django 入門', '佐々木 磨生', '龍澤出版', 350),
    ]

    # 返すHTMLは templates フォルダ以降のパスを書きます。
    return render_template('book/list.html', books=book_list)

@book_bp.route('/addition')
def book_addition():
    return render_template('addition/addition.html')

@book_bp.route('/addition', methods=['POST'])
def addition_button():
    
    # db追加
    title = request.form.get('title')
    author = request.form.get('author')
    publisher =  request.form.get('publisher')
    publicationYear = request.form.get('publicationYear')

    # if book_name == '':
    #     error = 'ユーザ名が未入力です。'
    #     return render_template('register.html', error=error, user_name=book_name, password=password)
    # if password == '':
    #     error = 'パスワードが未入力です。'
    #     return render_template('register.html', error=error)

    count = db.insert_book(title,author,publisher,publicationYear)

    # msg作成
    if count == 1:
        return render_template('book/list.html')
    else:
        return render_template('addition/addition.html')



