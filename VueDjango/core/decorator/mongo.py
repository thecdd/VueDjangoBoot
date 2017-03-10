import datetime
from mongoengine import signals


def handler(event):
    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls

        fn.apply = apply
        return fn

    return decorator


@handler(signals.pre_save)
def update_system_info(sender, document):
    if hasattr(document, 'updateTime'):
        document.updateTime = datetime.datetime.utcnow()
    if hasattr(document, 'version'):
        document.version += 1
