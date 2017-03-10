import datetime
from mongoengine import *
from VueDjango import env
from core.decorator.mongo import update_system_info

# register connection for mongoengine
connect(env.DB_CONFIG.get('mongodb').get('db')
        , host=env.DB_CONFIG.get('mongodb').get('host')
        , read_preference=True)


class UpdateDocument:
    createTime = DateTimeField(default=datetime.datetime.utcnow())
    updateTime = DateTimeField(default=datetime.datetime.utcnow())
    version = IntField(default=0)


@update_system_info.apply
class UserCredential(Document, UpdateDocument):
    password = StringField()
    encryptionKey = StringField()
    identificationID = StringField()
    userIPs = ListField()
    remark = StringField()

    meta = {
        'collection': 'fm_user_credential',
        'indexes': [
            {'fields': ['identificationID']},
            {'fields': ['userIPs']},
        ],
    }


class UserData(EmbeddedDocument):
    data = StringField()
    key = StringField()


@update_system_info.apply
class UserDataStore(Document, UpdateDocument):
    identificationID = StringField()
    dataStore = EmbeddedDocumentListField(UserData)

    meta = {
        'collection': 'fm_user_credential',
        'indexes': [
            {'fields': ['identificationID']},
        ],
    }


@update_system_info.apply
class UserRequestLog(Document, UpdateDocument):
    path = StringField()
    ip = StringField()

    meta = {
        'collection': 'fm_user_request_log',
        'indexes': [
            {'fields': ['ip']},
            {'fields': ['path']},
        ],
    }
