from sqlalchemy import Column, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

# データベースのベースクラスを定義
Base = declarative_base()

# Locationモデルを定義
class Location(Base):
    __tablename__ = 'locations'
    
    # 主キーとしてUUIDを使用し、デフォルト値をuuid.uuid4に設定
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # ユーザー名を格納するカラム。nullを許可しない場合はnullable=Falseを追加
    user_name = Column(String, nullable=False)
    
    # 緯度を格納するカラム。制約を追加する場合はnullable=Falseなどを使用
    latitude = Column(Float, nullable=False)
    
    # 経度を格納するカラム。制約を追加する場合はnullable=Falseなどを使用
    longitude = Column(Float, nullable=False)