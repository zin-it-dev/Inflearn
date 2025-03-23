from flask import request, url_for, flash, redirect, jsonify
from flask_login import login_user

from .dao import UserRepository, AnalyticsRepository
from .utils import generate_color_palette

user_repo = UserRepository()
analy_repo = AnalyticsRepository()


def login():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = request.form.get("remember")

    user = user_repo.auth_user(email=email, password=password)

    if user and user.is_admin:
        login_user(user, remember=remember)
        flash("Welcome, admin! You are successfully logged in.", "success")
    else:
        flash("Invalid email or password. Please try again.", "warning")

    return redirect(url_for("admin.index"))


def chart_new_users():
    queryset = analy_repo.stats_new_users()

    labels = [entry.month for entry in queryset]
    values = [entry.count for entry in queryset]

    colors = generate_color_palette(len(values))

    return jsonify(
        {
            "title": "📊 Number of New Users 📊",
            "data": {
                "labels": labels,
                "datasets": [
                    {
                        "label": "👤 New Users",
                        "backgroundColor": colors,
                        "borderColor": [color.replace("0.5", "1") for color in colors],
                        "data": values,
                    }
                ],
            },
        }
    )


def chart_user_activity():
    queryset = analy_repo.stats_user_active()

    labels = [entry.date for entry in queryset]
    values = [entry.count for entry in queryset]

    colors = generate_color_palette(len(values))

    return jsonify(
        {
            "title": "📅 Daily User Activity 📅",
            "data": {
                "labels": labels,
                "datasets": [
                    {
                        "label": "⚡ User Activity",
                        "backgroundColor": colors,
                        "borderColor": [color.replace("0.5", "1") for color in colors],
                        "data": values,
                    }
                ],
            },
        }
    )
