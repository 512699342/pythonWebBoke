from models.boke import Boke
from models.star import Star
from routes import *


main = Blueprint('boke', __name__)

Model = Boke


@main.route('/')
@login_required
def index():
    u = current_user()
    ms = u.boke
    return render_template('boke.html', boke_list=ms, user_id=u.id)


@main.route('/new')
@login_required
def new():
    return render_template('boke_new.html')


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    ip = request.remote_addr
    m.see_add(ip)
    m.save()
    u = current_user()
    star = Star.query.filter_by(user_id=u.id, boke_id=m.id).first()
    if star == None:
        star_flag = -1
    else:
        star_flag = star.flag
    return render_template('boke_index.html', boke=m,s_f=star_flag)


@main.route('/edit/<id>')
@login_required
def edit(id):
    t = Model.query.get(id)
    return render_template('boke_edit.html', todo=t)


@main.route('/add', methods=['POST'])
@login_required
def add():
    form = request.form
    m = Model(form)
    m.user_id = current_user().id
    m.save()
    return redirect(url_for('.index'))


@main.route('/update/<int:id>', methods=['POST'])
@login_required
def update(id):
    form = request.form
    t = Model.query.get(id)
    t.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
@login_required
def delete(id):
    t = Model.query.get(id)
    t.delete()
    return redirect(url_for('.index'))
