from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

from .api import Api

debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt = JWTManager()


authorizations = {
    "jwt": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token",
    }
}

api = Api(
    title="Inflearn 인프런 🎓",
    version="1.0.0",
    description="API for Inflearn 인프런 💻🎓🖥️📚📡🧑‍💻🎨",
    doc="/",
    contact="zin.it.dev@gmail.com",
    contact_email="zin.it.dev@gmail.com",
    license="Apache 2.0",
    terms_url="https://www.google.com/policies/terms/",
    authorizations=authorizations,
    validate=True,
    ordered=True,
)

cors = CORS(resources={r"/*": {"origins": "*"}})
