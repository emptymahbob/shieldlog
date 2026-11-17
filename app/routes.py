from flask import Blueprint, flash, redirect, render_template, request, url_for

from app import db
from app.models import Finding

bp = Blueprint("main", __name__)


@bp.route("/")
def dashboard():
    findings = Finding.query.order_by(Finding.created_at.desc()).all()
    stats = {
        "total": len(findings),
        "open": sum(1 for f in findings if f.status == "open"),
        "investigating": sum(1 for f in findings if f.status == "investigating"),
        "resolved": sum(1 for f in findings if f.status == "resolved"),
        "critical_high": sum(1 for f in findings if f.severity in ("critical", "high")),
    }
    return render_template("dashboard.html", findings=findings, stats=stats)


@bp.route("/findings/new", methods=["GET", "POST"])
def create_finding():
    if request.method == "POST":
        finding = Finding(
            title=(request.form.get("title") or "").strip(),
            description=(request.form.get("description") or "").strip(),
            category=request.form.get("category") or "other",
            severity=request.form.get("severity") or "medium",
            status=request.form.get("status") or "open",
        )
        if not finding.title:
            flash("Title is required.", "error")
            return render_template("finding_form.html", finding=finding, mode="create")

        if finding.category not in Finding.CATEGORIES:
            finding.category = "other"
        if finding.severity not in Finding.SEVERITIES:
            finding.severity = "medium"
        if finding.status not in Finding.STATUSES:
            finding.status = "open"

        db.session.add(finding)
        db.session.commit()
        flash("Finding logged.", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("finding_form.html", finding=None, mode="create")


@bp.route("/findings/<int:finding_id>")
def view_finding(finding_id: int):
    finding = Finding.query.get_or_404(finding_id)
    return render_template("finding_detail.html", finding=finding)


@bp.route("/findings/<int:finding_id>/edit", methods=["GET", "POST"])
def edit_finding(finding_id: int):
    finding = Finding.query.get_or_404(finding_id)
    if request.method == "POST":
        finding.title = (request.form.get("title") or "").strip()
        finding.description = (request.form.get("description") or "").strip()
        finding.category = request.form.get("category") or finding.category
        finding.severity = request.form.get("severity") or finding.severity
        finding.status = request.form.get("status") or finding.status

        if not finding.title:
            flash("Title is required.", "error")
            return render_template("finding_form.html", finding=finding, mode="edit")

        if finding.category not in Finding.CATEGORIES:
            finding.category = "other"
        if finding.severity not in Finding.SEVERITIES:
            finding.severity = "medium"
        if finding.status not in Finding.STATUSES:
            finding.status = "open"

        db.session.commit()
        flash("Finding updated.", "success")
        return redirect(url_for("main.view_finding", finding_id=finding.id))

    return render_template("finding_form.html", finding=finding, mode="edit")


@bp.route("/findings/<int:finding_id>/delete", methods=["POST"])
def delete_finding(finding_id: int):
    finding = Finding.query.get_or_404(finding_id)
    db.session.delete(finding)
    db.session.commit()
    flash("Finding deleted.", "success")
    return redirect(url_for("main.dashboard"))
