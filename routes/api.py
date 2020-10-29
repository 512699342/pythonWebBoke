from models.boke import Boke
from models.star import Star
from routes import *


main = Blueprint('api', __name__)

Model = Boke

@main.route('/book_thumb_add/<int:id>')
@login_required
def book_thumb_add(id):
    boke = Boke.query.get(id)
    boke.thumbs += 1
    boke.save()
    return 'true'

@main.route('/book_star/<int:id>', methods=['GET'])
@login_required
def book_star(id):
    u = current_user()
    boke = Boke.query.get(id)
    star = Star.query.filter_by(user_id=u.id, boke_id=boke.id).first()
    if star == None:
        star = Star(u.id, boke.id)
    else:
        star.flag = -star.flag
    boke.star_num += star.flag
    star.save()
    boke.save()
    return 'true'