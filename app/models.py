from datetime import datetime, timezone

from app import db


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Finding(db.Model):
    __tablename__ = "findings"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False, default="")
    category = db.Column(db.String(50), nullable=False, default="other")
    severity = db.Column(db.String(20), nullable=False, default="medium")
    status = db.Column(db.String(30), nullable=False, default="open")
    created_at = db.Column(db.DateTime, nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=utcnow, onupdate=utcnow)

    CATEGORIES = ("phishing", "malware", "misconfig", "access", "other")
    SEVERITIES = ("low", "medium", "high", "critical")
    STATUSES = ("open", "investigating", "resolved")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "severity": self.severity,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
