from core.tool.view_helper import render_view

BASE_TEMPLATE_PATH = 'index/app/'


def view_index(request, *arg, **dir):
    return render_view(request, BASE_TEMPLATE_PATH + 'index/index.html')
