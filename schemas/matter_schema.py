# schemaではシリアライズを行う
# シリアライズとは、 <User John Doe> -> {name: 'John Doe'}とJson化すること
# 反対にデシリアライズもできる
from api.database import ma
from models.matters import Matter

class MatterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Matter
