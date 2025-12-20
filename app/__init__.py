from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .auth.routes import bp as auth_bp
    from .dashboard.routes import bp as dashboard_bp
    from .courses.routes import bp as courses_bp
    from .grades.routes import bp as grades_bp
    from .announcements.routes import bp as announcements_bp
    from .profile.routes import bp as profile_bp
    from .search.routes import bp as search_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(grades_bp)
    app.register_blueprint(announcements_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(search_bp)

    from .seed import seed_demo_data

    @app.cli.command("seed")
    def seed_command():
        seed_demo_data()
        print("✅ Seeded demo data.")

    return app
