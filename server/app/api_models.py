from flask_restx import fields
from datetime import datetime, timezone

from .extensions import api

base = api.model(
    "API Response",
    {
        "id": fields.String(description="Unique identifier"),
        "is_active": fields.Boolean(
            description="Indicates whether is activated", example=True, default=True
        ),
        "date_created": fields.DateTime(
            description="The date created",
            example="2024-01-01",
            dt_format="rfc822",
            default=datetime.now(timezone.utc),
        ),
        "date_updated": fields.DateTime(
            description="The date updated",
            example="2024-01-01",
            dt_format="rfc822",
            default=datetime.now(timezone.utc),
        ),
    },
)

tag = api.clone(
    "Tag",
    base,
    {
        "tags": fields.List(
            fields.String, description="The course tags", example="#tech, #react,..."
        ),
    },
)

category = api.clone(
    "Category",
    base,
    {
        "name": fields.String(
            readonly=True, description="The category name", example="Web Development"
        ),
    },
)

course = api.clone(
    "Course",
    tag,
    {
        "title": fields.String(
            readonly=True, description="The course title", example="Grocery Shopping"
        ),
        "description": fields.String(
            readonly=True,
            description="A detailed description of the course",
            example="Buy milk, eggs, and bread",
        ),
        "category": fields.String(
            attribute="category.name",
            readonly=True,
            description="The course category",
            example="Frameworks, Languages / Platforms,...",
        ),
        "tags": fields.List(
            fields.String, description="The course tags", example="#tech, #react,..."
        ),
        "lessons": fields.Integer(
            attribute="total_lessons",
            readonly=True,
            description="Total number of lessons in the course",
            example=10,
        ),
    },
)

pagination = api.model(
    "Pagination",
    {"count": fields.Integer(description="Total items of the model", example="1000")},
)

courses = api.clone(
    "Courses",
    pagination,
    {
        "results": fields.List(fields.Nested(course)),
    },
)

lesson = api.clone(
    "Lesson",
    tag,
    {
        "title": fields.String(
            readonly=True, description="The lesson title", example="Grocery Shopping"
        ),
        "content": fields.String(
            readonly=True,
            description="A detailed content of the lesson",
            example="Buy milk, eggs, and bread",
        ),
    },
)

lessons = api.clone(
    "Lessons",
    pagination,
    {
        "results": fields.List(fields.Nested(lesson)),
    },
)

login = api.model(
    "Log In",
    {
        "email": fields.String(required=True, example="<user>infl@gmail.com"),
        "password": fields.String(required=True, example="password [Aa-zZ][0-9]"),
    },
)

profile = api.clone(
    "Current User",
    {
        "username": fields.String(required=True, example="juxjor"),
        "email": fields.String(required=True, example="<user>infl@gmail.com"),
        "avatar": fields.String(description="URL to the user's profile avatar"),
        "first_name": fields.String(
            required=True, description="The user first name", example="David"
        ),
        "last_name": fields.String(required=True, description="The user last name", example="Adam"),
    },
)

user = api.clone(
    "User",
    profile,
    {
        "password": fields.String(required=True, example="password [Aa-zZ][0-9]"),
    },
)

comment = api.clone(
    "Comment",
    base,
    {
        "content": fields.String(
            required=True, description="The comment content", example="So good"
        ),
        "user": fields.String(
            attribute="user",
            readonly=True,
            description="The comment user",
            example="david, alan, john...",
        ),
    },
)

enable_2fa = api.model(
    "Enable2FA", {"user_id": fields.Integer(required=True, description="User ID")}
)

verify_totp = api.model(
    "VerifyTOTP",
    {
        "user_id": fields.Integer(required=True, description="User ID"),
        "totp_code": fields.String(required=True, description="TOTP code"),
    },
)
