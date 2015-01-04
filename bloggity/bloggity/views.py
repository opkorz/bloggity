from flask import Blueprint, redirect, render_template, request, Response

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
  return render_template("index.html")