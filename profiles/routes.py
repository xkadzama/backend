from flask import Blueprint, render_template

from flask_login import login_required, current_user


profile_bp = Blueprint('profile', __name__, template_folder='templates')


@profile_bp.route('/') # /profile/
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)