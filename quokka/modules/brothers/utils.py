# coding: utf-8

from flask import current_app, request
from .models import BrotherInfo as Brother

def get_brothers(*args, **kwargs):
    brothers = Brother.objects.order_by(current_app.config.get(BROTHERS_ORDER", "name"))
    
    disabled_pagination = False
    if not current_app.config.get("BROTHERS_PAGINATION_ENABLED", True):
        disabled_pagination = authors.count()

    pagination_arg = current_app.config.get("PAGINATION_ARG", "page")
    page = request.args.get(pagination_arg, 1)
    per_page = (
        disabled_pagination or
        request.args.get('per_page') or
        current_app.config.get("AUTHORS_PAGINATION_PER_PAGE", 20)
    )
    brothers = brothers.paginate(page=int(page),
                               per_page=int(per_page))
    return brothers


def get_brother(brother_id):
    try:
        brother = Brother.objects.get(id=brother_id)
    except:
        brother = Brother.objects.get(username=brother_id)
    return author
