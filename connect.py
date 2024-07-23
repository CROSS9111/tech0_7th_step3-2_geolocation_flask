# # uname() error回避
# import platform
# print(platform.uname())

# from sqlalchemy import create_engine
# import sqlalchemy

# import os
# main_path = os.path.dirname(os.path.abspath(__file__))
# path = os.chdir(main_path)
# print(path)
# engine = create_engine("sqlite:///CRM.db", echo=True)

# uname() error回避
import platform
print(platform.uname())

from sqlalchemy import create_engine
import os

# 現在のファイルのディレクトリを取得し、カレントディレクトリを変更
main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)
print(f"Current directory: {main_path}")

# SQLiteデータベースエンジンを作成（データベース名をgeoに変更）
engine = create_engine("sqlite:///geo.db", echo=True)

