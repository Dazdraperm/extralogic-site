"""
Basic views to filling data of Form
"""
from flask import Blueprint, Response

bp = Blueprint('form', __name__, url_prefix='/form')


@bp.route('/<form_uid>', methods=['GET'])
def get_form(form_uid):
    return Response(status=200)


@bp.route('/<form_uid>', methods=['POST'])
def save_form_data(form_uid):
    pass
