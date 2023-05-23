from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/execute-script', methods=['GET'])
def execute_script():
    try:
        print("IM DOIING IT")
        subprocess.call(['./create_next_cluster.sh'])
        print("created sub_process")
        return 'Script executed successfully'
    except Exception as e:
        print("I failed")
        return f'Failed to execute script: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

