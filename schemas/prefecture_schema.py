# schemaではシリアライズを行う
# シリアライズとは、 <User John Doe> -> {name: 'John Doe'}とJson化すること
# 反対にでシリアライズもできる
from api.database import ma
from models.prefectures import Prefecture

class PrefectureSchema(ma.SQLAlchemyAutoSchema):
    region_name = ma.String()
    class Meta:
        model = Prefecture
        load_instance = True
