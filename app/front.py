from os.path import exists
from flask import Blueprint, request, render_template, make_response
from flask_cors import cross_origin

bp = Blueprint('frontend-endpoints', __name__, url_prefix='/')

# TODO
#  СЮДА СДЕЛАТЬ ВСЕ GET ЗАПРОСЫ
# НЕ ЗАБЫТЬ ПРОВЕРКУ АВТОРИЗАЦИИ НА ЗАКРЫТЫЕ ЭНДПОИНТЫ
# GET ЗАПРОС ДЛЯ LOGOUT СДЕЛАЕМ ЗДЕСЬ, ТАМ ОСТАВИМ POST 