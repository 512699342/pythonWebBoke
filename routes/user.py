# from models.user import User
from routes import *


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是套路
main = Blueprint('user', __name__)
Model = User


def range_cookie(m=20):

    n = m
    s = ""
    for i in range(n):
        s += chr(97 + random.randint(0, 25))
    print("s cookie", s)
    return s


# def set_cookie_session(user):
#     cookie = range_cookie()
#     session[cookie] = user.id


@main.route('/')
def login_view():
    u = current_user()
    if u is not None:
        return redirect(url_for('boke.index', id=u.id))
    return render_template('login.html')


@main.route('register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    print(u.valid())
    cookie = ""
    if u.valid()[0]:
        u.save()
        cookie = range_cookie()
        session[cookie] = u.id
    else:
        abort(400)
    # 蓝图中的 url_for 需要加上蓝图的名字，这里是 user
    response = redirect(url_for('.login_view'))
    response.set_cookie('user_id', cookie)
    return response


@main.route('login', methods=['POST'])
def login():
    form = request.form
    print('from', form)
    u = User(form)
    print("login from", form, u)
    # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
    user = User.query.filter_by(username=u.username).first()
    cookie = ""
    # if user is not None and user.validate_login(u):
    if u.valid_login(user):
        print('登录成功')
        cookie = range_cookie()
        session[cookie] = user.id
    else:
        print('登录失败')
    # 蓝图中的 url_for 需要加上蓝图的名字，这里是 user
    response = redirect(url_for('.login_view'))
    response.set_cookie('user_id', cookie)
    return response


@main.route('update', methods=['POST'])
def update():
    u = current_user()
    password = request.form.get('password', '123')
    if u.change_password(password):
        print('修改成功')
    else:
        print('用户密码修改失败')
    return redirect('/user/profile')


@main.route('profile', methods=['GET'])
def profile():
    u = current_user()
    if u is not None:
        print('profile', u.id, u.username, u.password)
        return render_template('profile.html', user=u)
    else:
        abort(401)


@main.route('logoff/<int:id>', methods=['GET'])
@login_required
def logoff(id):
    u = current_user()
    if u.id != id:
        print('注销用户失败')
        abort(404)
    else:
        cookie = request.cookies.get('user_id', None)
        del session[cookie]
        response = redirect(url_for('.login_view'))
        response.delete_cookie('user_id')
        print('注销用户成功 cookie', response.headers.__dict__)
    return response
