from flask import Blueprint,render_template

sports_bp = Blueprint('sport_bp',__name__)


@sports_bp.route('/sports')
def index():
    return render_template("sports.html")