from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/list')
def user_list():
    user_list = [
        (1, '佐々木 磨生', 'sasaki@morijyobi.ac.jp'),
        (2, '細川 潤哉', 'hosokawa@morijyobi.ac.jp'),
        (3, '高橋 洋平', 'takahashi@morijyobi.ac.jp')
    ]
    return render_template('user/list.html', users=user_list)
