# schemaではシリアライズを行う
# シリアライズとは、 <User John Doe> -> {name: 'John Doe'}とJson化すること
# 反対にでシリアライズもできる
from api.database import ma
from models.users import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
