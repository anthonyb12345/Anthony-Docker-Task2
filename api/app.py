from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
from io import BytesIO
import os

app = Flask(__name__)

minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ROOT_USER'),
    secret_key=os.getenv('MINIO_ROOT_PASSWORD'),
    secure=False
)

bucket_name = "mybucket"


@app.route('/store', methods=['POST'])
def store():
    data = request.json
    object_name = data.get("name")
    content = request.data  # Get the raw data from the request

    try:
        # Open a BytesIO stream
        data_stream = BytesIO(content)

        # Use put_object with the BytesIO stream
        minio_client.put_object(bucket_name, object_name, data_stream, len(content))
        
        return jsonify({"message": "Data stored successfully"}), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    app.run(host='0.0.0.0', port=5000)