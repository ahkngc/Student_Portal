from flask import Blueprint, render_template, request, redirect, url_for, flash
from .services import login_user, logout_user, get_current_user

bp = Blueprint("auth", __name__)

@bp.get("/")
def home():
    return redirect(url_for("dashboard.dashboard")) if get_current_user() else redirect(url_for("auth.login"))

@bp.route("/login", methods=["GET", "POST"])
def login():
    if get_current_user():
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":
        user = login_user(request.form.get("email", ""), request.form.get("password", ""))
        if not user:
            flash("Invalid email or password", "danger")
            return render_template("login.html", user=None)

        flash(f"Welcome, {user.name}!", "success")
        return redirect(url_for("dashboard.dashboard"))

    return render_template("login.html", user=None)

@bp.post("/logout")
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))
