from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:[password]@cluster0.8s2if.mongodb.net/Clustoer0?retryWrites=true&=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket.find({}, {'_id': False}))      # list()는 배열 만들기라고 생각하기. db의 bucket 테이블에서 find
    count = len(bucket_list) + 1                                # len()은 배열의 개수 구하기. .length()와 같은 기능

    doc = {
        'num':count,
        'bucket':bucket_receive,
        'done':0
    }

    db.bucket.insert_one(doc)

    return jsonify({'msg': 'submit complete!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST(완료) 연결 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
