import json
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from VueDjango.env import SITE_CONFIG


def get_common_template_context(extra_context=None):
    base_context = {
        'BASE_URL_PATH': SITE_CONFIG.get('base_url'),
        'STATIC_URL_PATH': SITE_CONFIG.get('static_url')
    }
    if extra_context is not None:
        base_context.update(extra_context)

    return base_context


def render_view(request, template_path, context=None):
    view_context = get_common_template_context()
    if context is not None:
        view_context.update(context)
    return render(request, template_path, view_context)


def render_api(data, resp_status=status.HTTP_200_OK, is_json=True):
    if is_json:
        return HttpResponse(json.dumps(data), status=resp_status, content_type='application/json')
    else:
        return Response(data, status=resp_status)
