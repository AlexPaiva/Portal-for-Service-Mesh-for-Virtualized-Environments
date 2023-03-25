import time
from flask import Flask, jsonify
import random
import threading

app = Flask(__name__)
factory_data = {"material_in": 50, "product_out": 50}

def update_data():
    global factory_data
    while True:
        material_in = random.randint(1, 99)
        product_out = 100 - material_in
        factory_data = {
            "material_in": material_in,
            "product_out": product_out,
        }
        time.sleep(1)

@app.route('/api/data')
def get_factory_data():
    return jsonify(factory_data)

if __name__ == '__main__':
    data_updater = threading.Thread(target=update_data)
    data_updater.start()
    app.run(host='0.0.0.0', port=80)
