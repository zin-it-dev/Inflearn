from flask import flash, jsonify
from flask_babel import gettext

from .models import db


def make_active(self=None, ids=None):
    try:
        query = self.get_query().filter(self.model.id.in_(ids))
        count = 0

        for model in query.all():
            model.active = not model.active if model else True
            count += 1

        db.session.commit()
        flash(gettext(f"Successfully activated {count} models."), category="success")
    except Exception as e:
        flash(gettext(f"Failed to activate status. {str(e)}"), category="error")
