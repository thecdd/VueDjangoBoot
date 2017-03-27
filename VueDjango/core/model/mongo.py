import datetime
from mongoengine import *
from VueDjango import env
from core.decorator.mongo import update_system_info
from core.tool.encryption_tools import encrypt_psw

connect(env.DB_CONFIG.get('mongodb').get('db')
        , host=env.DB_CONFIG.get('mongodb').get('host')
        , read_preference=True)


class UpdateDocument:
    createBy = StringField()
    createTime = DateTimeField(default=datetime.datetime.utcnow())
    updateBy = StringField()
    updateTime = DateTimeField(default=datetime.datetime.utcnow())
    version = IntField(default=0)


@update_system_info.apply
class User(Document, UpdateDocument):
    userID = StringField()
    password = StringField()
    encryptionKey = StringField()
    email = StringField()
    firstName = StringField()
    lastName = StringField()
    lastLoginTime = DateTimeField()

    def set_password(self, new_password):
        password, encryption_key = encrypt_psw(new_password)
        self.password = password
        self.encryptionKey = encryption_key

    def verify(self, user_password):
        user_encrypt_password, encryption_key = encrypt_psw(user_password, self.encryptionKey)
        return user_encrypt_password == self.password

    meta = {
        'collection': 'gvvmc_dsh_user',
    }
