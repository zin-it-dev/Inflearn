from flask import Flask
from flask_login import current_user
from datetime import datetime, timezone

from .config import settings
from .extensions import migrate, api, login_manager, jwt, cors, mail, debug_toolbar
from .models import db
from .admin import admin_manager, babel
from .resources import category_ns, course_ns, auth_ns, user_ns, comment_ns
from .dao import UserRepository
from .controllers import login, chart_new_users, chart_user_activity

user_repo = UserRepository()


def create_app(config_name="development"):
    app = Flask(__name__)

    app.config.from_object(settings[config_name])

    if app.debug:
        debug_toolbar.init_app(app)

    app.add_url_rule("/login", view_func=login, methods=["POST"])

    # Statistics
    app.add_url_rule("/charts/new-users", view_func=chart_new_users, methods=["GET"])
    app.add_url_rule("/charts/user-activity", view_func=chart_user_activity, methods=["GET"])

    db.init_app(app)
    migrate.init_app(app, db)
    admin_manager.init_app(app)
    babel.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)

    mail.init_app(app)
    cors.init_app(app)
    api.init_app(app)
    api.add_namespace(category_ns)
    api.add_namespace(course_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(comment_ns)

    @app.before_request
    def before_request():
        if current_user.is_authenticated:
            current_user.last_seen = datetime.now(timezone.utc)
            current_user.save()

    @login_manager.user_loader
    def loader_user(user_id):
        return user_repo.get_by_id(id=user_id)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return user_repo.get_callback(identity)

    return app
