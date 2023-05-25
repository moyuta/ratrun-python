# schemaではシリアライズを行う
# シリアライズとは、 <User John Doe> -> {name: 'John Doe'}とJson化すること
# 反対にでシリアライズもできる
from api.database import ma
from models.jobs import Job

class JobSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Job
