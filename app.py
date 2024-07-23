
from flask import Flask, request
from flask import jsonify
import json
from flask_cors import CORS
import crud, mymodels
import requests

app = Flask(__name__)

CORS(app)

@app.route("/")
def index():
    return "<p>Flask top page!</p>"


@app.route("/locations", methods=["POST"])
def locations():
    try:
        # リクエストからデータを取得
        data = request.json
        print(data)
        payload = data.get("payload")
        if payload:
            user_name = payload.get("user_name")
            latitude = payload.get("latitude")
            longitude = payload.get("longitude")
            print(f"user_name: {user_name}, latitude: {latitude}, longitude: {longitude}")

            # データベースに書き込み
            values = {
                "user_name": user_name,
                "latitude": latitude,
                "longitude": longitude
            }
            crud.myinsert(mymodels.Location, values)

            # データベースからすべてのレコードを読み取り
            locations = crud.myload_by_user(mymodels.Location, user_name)
        
            # 結果をJSON形式でフロントエンドに返信
            locations_list = [{"user_name": loc.user_name, "latitude": loc.latitude, "longitude": loc.longitude} for loc in locations]
            return jsonify(locations_list), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



# -- SQLite
# INSERT INTO locations (id, user_name, latitude, longitude)
# VALUES ('995fd14f0b6f4d469c927e0c14ec60d2', 'kurosu', 35.2185993, 138.354009);