from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('classifier', __name__, url_prefix='/classifier')


@bp.route('/fcsClassfier', methods=('GET', 'POST'))
def register():
    return render_template('base.html')
