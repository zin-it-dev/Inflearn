from flask import jsonify
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, current_user, create_access_token, create_refresh_token
from datetime import datetime, timezone

from .api_models import (
    category,
    courses,
    course,
    lessons,
    lesson,
    login,
    user,
    profile,
    comment,
    enable_2fa,
    verify_totp,
)
from .dao import (
    CategoryRepository,
    CourseRepository,
    LessonRepository,
    UserRepository,
    CommentRepository,
)
from .parsers import CourseParser, LessonParser, UserParser
from .errors import APIException
from .utils import upload_image, generate_totp, handle_verify_totp

category_ns = Namespace("categories", description="Operations related to categories")
course_ns = Namespace("courses", description="Operations related to courses")
auth_ns = Namespace("auth", description="Operations related to authentication")
user_ns = Namespace("users", description="Operations related to users")
comment_ns = Namespace("comments", description="Operations related to comments")

category_repo = CategoryRepository()
course_repo = CourseRepository()
lesson_repo = LessonRepository()
user_repo = UserRepository()
comment_repo = CommentRepository()

course_parser = CourseParser().parser
lesson_parser = LessonParser().parser
user_parser = UserParser().parser

secret_keys = {}


@category_ns.route("/")
class CategoryList(Resource):
    @category_ns.doc("category_list")
    @category_ns.marshal_list_with(category)
    def get(self):
        """
        List all categories

        Implementation to retrieve and return all categories
        """
        return category_repo.get_all()


@course_ns.route("/")
class CourseList(Resource):
    @course_ns.doc("course_list")
    @course_ns.marshal_list_with(courses)
    @course_ns.expect(course_parser)
    def get(self):
        """
        List all courses

        Implementation to retrieve and return a list of courses
        """
        args = course_parser.parse_args()
        return course_repo.get_all(**args)


@course_ns.route("/<int:id>")
class Course(Resource):
    @course_ns.doc("course_retrieve")
    @course_ns.marshal_with(course)
    def get(self, id):
        """
        Get a specific course by ID

        Implementation to retrieve and return a course by ID
        """
        if not course_repo.get_by_id(id):
            raise APIException(f"Course ID {id} not found !!!", status_code=404)

        return course_repo.get_by_id(id)


@course_ns.route("/<int:id>/lessons/")
class LessonList(Resource):
    @course_ns.doc("course_lesson_list")
    @course_ns.marshal_with(lessons)
    @course_ns.expect(lesson_parser)
    def get(self, id):
        """
        List all lessons

        Implementation to retrieve and return a list of lessons
        """
        if not course_repo.get_by_id(id):
            raise APIException(f"Course ID {id} not found !!!", status_code=404)

        args = lesson_parser.parse_args()
        return lesson_repo.get_all(id, **args)


@course_ns.route("/<int:id>/lessons/<int:lesson_id>")
class Lesson(Resource):
    @course_ns.doc("course_lesson_retrieve")
    @course_ns.marshal_with(lesson)
    def get(self, id, lesson_id):
        """
        Get a specific lesson by ID

        Implementation to retrieve and return a lesson by ID
        """
        if not course_repo.get_by_id(id):
            raise APIException(f"Course ID {id} not found !!!", status_code=404)

        args = lesson_parser.parse_args()
        if not lesson_repo.get_all(id, lesson_id, **args):
            raise APIException(f"Lesson ID {id} not found !!!", status_code=404)

        return lesson_repo.get_all(id, lesson_id, **args)


@auth_ns.route("/token/")
class Token(Resource):
    @auth_ns.doc("token_retrieve")
    @auth_ns.expect(login)
    def post(self):
        """
        Authenticate user and generate access & refresh tokens.

        Allows users to log in by providing their email and password.

        If the credentials are valid, it returns an access token (for authentication) and a refresh token (to obtain a new access token when expired).
        """

        user = user_repo.auth_user(
            email=auth_ns.payload["email"], password=auth_ns.payload["password"]
        )

        if not user:
            raise APIException("Invalid email or password !!!", status_code=401)

        access_token = create_access_token(identity=user, fresh=True)
        refresh_token = create_refresh_token(identity=user)
        
        user.last_seen = datetime.now(timezone.utc)
        user.save()

        return jsonify(
            access_token=access_token,
            refresh_token=refresh_token,
            httponly=True,
            secure=True,
            samesite="Strict",
        )


@auth_ns.route("/current-user/")
class CurrentUser(Resource):
    method_decorators = [jwt_required(optional=True)]

    @auth_ns.doc("current_user_retrieve", security="jwt")
    @auth_ns.marshal_with(profile, code=200)
    def get(self):
        """
        Retrieve the current authenticated user's profile.

        Returns the profile information of the currently authenticated user.

        A valid JWT access token is required in the `Authorization` header.
        """
        if not current_user:
            raise APIException("Missing Authorization Header !!!", status_code=401)

        return user_repo.get_by_id(id=current_user.id)


@auth_ns.route("/enable_2fa/")
class Enable2FA(Resource):
    @auth_ns.doc("enable_2fa_create")
    @auth_ns.expect(enable_2fa)
    def post(self):
        """Enables Two-Factor Authentication for a user."""
        user_id = auth_ns.payload["user_id"]
        secret_key, provisioning_uri, qr_code_base64 = generate_totp(user_id)
        secret_keys[user_id] = secret_key

        return {
            "qr_code": qr_code_base64,
            "secret_key": secret_key,
        }, 200


@auth_ns.route("/verify-totp/")
class VerifyTOTP(Resource):
    @auth_ns.doc("verify_otp_create")
    @auth_ns.expect(verify_totp)
    def post(self):
        """Enables Two-Factor Authentication for a user."""
        user_id = auth_ns.payload["user_id"]
        totp_code = auth_ns.payload["totp_code"]
        secret_key = secret_keys.get(user_id)

        if not secret_key:
            return {"message": "2FA not enabled for this user."}, 400

        if handle_verify_totp(secret_key, totp_code):
            return {"message": "TOTP code is valid!"}, 200
        else:
            return {"message": "TOTP code is invalid."}, 400


@user_ns.route("/")
class User(Resource):
    @user_ns.doc("user_create")
    @user_ns.expect(user_parser)
    @user_ns.marshal_with(user)
    def post(self):
        """
        Create a new user

        Implementation to create a new user
        """
        args = user_parser.parse_args()

        errors = user_repo.is_exists(args["email"], args["username"].lower())

        if errors:
            raise APIException("User with this email or username already exists.", status_code=400)

        avatar_url = None
        avatar = args["avatar"]

        if avatar:
            avatar_url = upload_image(file_data=avatar)

        new_user = user_repo.create(
            username=args["username"].lower(),
            email=args["email"],
            password=args["password"],
            first_name=args["first_name"],
            last_name=args["last_name"],
            avatar=avatar_url,
        )

        return new_user, 201


@comment_ns.route("/")
class commentList(Resource):
    @comment_ns.doc("comment_list")
    @comment_ns.marshal_list_with(comment)
    def get(self):
        """
        List all comments

        Implementation to retrieve and return all comments
        """
        return comment_repo.get_all()
