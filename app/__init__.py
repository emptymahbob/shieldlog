from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

db = SQLAlchemy()


def create_app() -> Flask:
    root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        template_folder=str(root / "templates"),
        static_folder=str(root / "static"),
    )
    app.config["SECRET_KEY"] = "shieldlog-dev-only-change-me"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{root / 'shieldlog.db'}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import bp

    app.register_blueprint(bp)

    with app.app_context():
        from app import models  # noqa: F401

        db.create_all()
        _seed_if_empty()

    return app


def _seed_if_empty() -> None:
    from app.models import Finding

    if Finding.query.count() == 0:
        samples = [
            Finding(
                title="Suspicious login from unusual location",
                description="User reported a login alert from a new country. MFA was successful; session reviewed and closed.",
                category="access",
                severity="medium",
                status="resolved",
            ),
            Finding(
                title="Open S3 bucket flagged in scan",
                description="Cloud scanner reported public read on a staging bucket. Access locked pending review.",
                category="misconfig",
                severity="high",
                status="investigating",
            ),
            Finding(
                title="Phishing email reported by staff",
                description="Lookalike invoice email. Links blocked at gateway; message quarantined.",
                category="phishing",
                severity="low",
                status="open",
            ),
        ]
        db.session.add_all(samples)
        db.session.commit()
