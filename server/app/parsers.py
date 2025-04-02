from flask_restx import reqparse, inputs
from werkzeug.datastructures import FileStorage


class BaseParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def parse_args(self):
        return self.parser.parse_args()


class CourseParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.add_argument("keyword", required=False, type=str, help="Search course by title")
        self.add_argument("category", type=int, required=False, help="Filter course by category")
        self.add_argument("page", type=int, required=False, default=1, help="Pagination course")


class LessonParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.add_argument("page", type=int, required=False, default=1, help="Pagination lesson")


class UserParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.add_argument("username", type=str, required=True)
        self.add_argument(
            "email", type=inputs.regex(r"^[a-zA-Z0-9_.+-]+@gmail\.com$"), required=True
        )
        self.add_argument("first_name", type=str, required=True)
        self.add_argument("last_name", type=str, required=True)
        self.add_argument(
            "password",
            type=inputs.regex(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"),
            required=True,
        )
        self.add_argument("avatar", required=False, type=FileStorage, location="files")
