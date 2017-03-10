from django.http import HttpResponseServerError
from django.http.request import HttpRequest
from core.model.mongo import *


class IPPermissionRequired:
    def __call__(self, fn):
        def wapper(*args, **kwargs):
            request = None
            for arg in args:
                if isinstance(arg, HttpRequest):
                    request = arg

            is_correct_visit = True
            content_type = 'application/json'

            if request is not None:
                path = request.path
                ip = request.META.get('REMOTE_ADDR')
                user_request_log = UserRequestLog()
                user_request_log.path = path
                user_request_log.ip = ip
                user_request_log.save()

                record = UserCredential.objects(Q(userIPs=ip))
                is_correct_visit = len(record) > 0

            if is_correct_visit:
                return fn(*args, **kwargs)
            else:
                return HttpResponseServerError(content_type=content_type)

        return wapper
