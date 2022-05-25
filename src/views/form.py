"""
Basic views to filling data of Form
"""
from flask import Blueprint, render_template

from src.json_rpc import JsonRPC

bp = Blueprint('form', __name__, url_prefix='/form')


@bp.route('/<form_uid>', methods=['GET'])
def get_form(form_uid):
    """
    Шаблон формы
    :param form_uid:
    :return:
    """
    json_rpc = JsonRPC()
    response = json_rpc.get_fields(form_uid=form_uid)
    fields_form = response.json().get('result')

    return render_template('form.html', fields_form=fields_form)


@bp.route('/filling/<form_uid>', methods=['GET'])
def get_filling_form(form_uid):
    """
    Форма с заполненным полем
    :param form_uid:
    :return:
    """
    json_rpc = JsonRPC()
    response = json_rpc.get_form_data(form_uid=form_uid)
    fields_form = response.json().get('result')

    return render_template('filling_form.html', fields_form=fields_form)
