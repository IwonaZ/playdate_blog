from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except:
        return None


class User(db.Document, UserMixin):
    #id = db.Column(db.Integer, primary_key=True)
    username = db.StringField(unique=True, nullable=False)
    email = db.EmailField(unique=True, nullable=False)
    image_file = db.StringField(nullable=False, default='default.jpg')
    password = db.StringField(nullable=False)
    posts = db.ReferenceField('Post')
    address = db.StringField(max_length=150, nullable=False)
    location = db.PointField()

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': str(self.id)}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
'''class Language(db.Document):
    language_name = db.StringField()
    
    def __repr__(self):
        return f"Language('{self.language_name}')"
    
    def language_list():
        language1 = Language(language_name = 'english')
        language2 = Language(language_name = 'german')
        language3 = Language(language_name = 'polish')'''
        
#language_choices = [('1', 'english'), ('2', 'german'), ('3', 'spanish')]
                
class Post(db.Document):
    #id = db.Column(db.Integer, primary_key=True)
    title = db.StringField(nullable=False)
    date_posted = db.DateTimeField(nullable=False, default=datetime.utcnow)
    content = db.StringField(nullable=False)
    user_id = db.ReferenceField('User')
    gender = db.StringField()
    age = db.IntField(nullable=False)
    language_learning = db.ListField(db.StringField())
    language_speaking = db.ListField(db.StringField())
    views = db.IntField(default=0)

    #lang = db.ListField(db.StringField(max_length=30))
    #language_learning = db.ListField(db.EmbeddedDocumentField('TestForm'))
    #language_speaking = db.ListField(db.EmbeddedDocumentField('TestForm'))


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    

'''class Language(db.Document):
    language_name = db.StringField()
    
    def __repr__(self):
        return f"Language('{self.language_name}')"'''
    