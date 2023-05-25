from flask import Flask, jsonify,request
from flask_restful import Api, Resource
from api import app
from models.users import User
from models.jobs import Job
from models.prefectures import Prefecture,Region
from models.matters import Matter, MatterProgrammingLanguage, MatterTitleChip, ProgrammingLanguage, TitleChip
from schemas.user_schema import UserSchema
from schemas.job_schema import JobSchema
from schemas.prefecture_schema import PrefectureSchema
from schemas.matter_schema import MatterSchema
from functions.forms import RegistrationForm,EditForm
from api.database import db
from flask_wtf.csrf import generate_csrf
from flask_login import current_user
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

api = Api(app)


class GetToken(Resource):
    def get(self):
        token = generate_csrf()
        return {'csrfToken': token}, 200

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        user_schema = UserSchema(many=True)
        return user_schema.jsonify(users)


class AuthResource(Resource):
    def post(self):
        # ログイン処理
        data = request.get_json()
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return {'message': 'ログインしました'}, 200
        else:
            return {'message': 'ログインに失敗しました'}, 401
    def delete(self):
        # ログアウト処理
        logout_user()
        return {'message': 'ログアウトしました'}, 200    


class MailRegisterResource(Resource):
    def post(self):
        data = request.get_json(force=True)
        form = RegistrationForm(data=data)
        if form.validate_on_submit():
            # バリデーション成功時の処理
            user = User(
            email=form.email.data,
            password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            return {'message': 'ユーザー登録に成功しました'}, 200
        else:
            # バリデーション失敗時の処理
            error_messages = {}
            for field, errors in form.errors.items():
                error_messages[field] = errors

            return {'message': 'ユーザー登録に失敗しました', 'errors': errors}, 400

    def dispatch_request(self, *args, **kwargs):
        try:
            resp = super().dispatch_request(*args, **kwargs)
            return resp
        except Exception as e:
            return {'message': str(e)}, 500

class RegisterResource(Resource):
    def post(self):
        data = request.get_json(force=True)
        form = EditForm(data=data)
        if form.validate_on_submit():
            user_id = current_user.id
            user = User.query.get(user_id)
            user.name, user.name_kana, user.phone, user.job_id, user.prefecture_id = data['name'], data['name_kana'], data['phone'], data['job_id'], data['prefecture_id']
            db.session.commit()
            return {'message': 'ユーザー登録に成功しました'}, 200
        else:
            # バリデーション失敗時の処理
            error_messages = {}
            for field, errors in form.errors.items():
                error_messages[field] = errors

            return {'message': 'ユーザー登録に失敗しました', 'errors': errors}, 400    
        
class ListJobsResource(Resource):
    def get(self):
        # 職種リスト関連の処理
         jobs = Job.query.all()
         job_schema = JobSchema(many=True)
         return job_schema.jsonify(jobs)


class ListPrefecturesResource(Resource):
    def get(self):
        # 都道府県リスト関連の処理
         query = db.session.query(Prefecture.id, Prefecture.name, Prefecture.name_kana,
                         Region.name.label('region_name'), Region.name_kana.label('region_name_kana'))\
                  .join(Region, Prefecture.region_id == Region.id)
         prefectures_and_regions = query.all()
         prefecture_and_region_schema = PrefectureSchema(many=True)
         return  prefecture_and_region_schema.jsonify(prefectures_and_regions)
    
class EditEmailResource(Resource):
    def post(self):
        data = request.get_json(force=True)
        form = RegistrationForm(data=data)
        if form.validate_on_submit():
            # バリデーション成功時の処理
            user_id = current_user.id
            user = User.query.get(user_id)
            if user.check_password(form.password.data):
                user.email = form.email.data
                db.session.commit()
                return {'message': 'ユーザー情報の更新に成功しました'}, 200
            else:
                return {'message': 'パスワードが正しくありません'}, 400
        else:
            # バリデーション失敗時の処理
            error_messages = {}
            for field, errors in form.errors.items():
                error_messages[field] = errors

            return {'message': 'ユーザー情報の更新に失敗しました', 'errors': errors}, 400

class MattersResource(Resource):
    def get(self):
        matters = Matter.query.outerjoin(MatterProgrammingLanguage).outerjoin(MatterTitleChip).outerjoin(ProgrammingLanguage).outerjoin(TitleChip).all()
        matter_schema = MatterSchema(many=True)
        return matter_schema.dump(matters)

api.add_resource(GetToken, '/v1/auth/token')
api.add_resource(UserResource, '/v1/users/all')
api.add_resource(AuthResource, '/v1/users/auth')
api.add_resource(MailRegisterResource, '/v1/users/mail_register')
api.add_resource(RegisterResource, '/v1/users/register')
api.add_resource(ListJobsResource, '/v1/users/list/jobs')
api.add_resource(ListPrefecturesResource, '/v1/users/list/prefectures')
api.add_resource(EditEmailResource, '/v1/users/edit_email')
api.add_resource(MattersResource, '/v1/matters/total_count')


