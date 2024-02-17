import time
from flask import Flask, jsonify
import random
import threading

app = Flask(__name__)
factory_data = {"material_in": 150, "product_out": 75}

def update_data():
    global factory_data
    while True:
        material_in = random.randint(135, 165)
        product_out = random.randint(67, 83)
        factory_data = {
            "material_in": material_in,
            "product_out": product_out,
        }
        time.sleep(3)

@app.route('/api/data')
def get_factory_data():
    return jsonify(factory_data)

if __name__ == '__main__':
    data_updater = threading.Thread(target=update_data)
    data_updater.start()
    app.run(host='0.0.0.0', port=80)
