from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    if data['iris_id'] == '123456789012' and data['pin'] == '123456':
        return jsonify({'status': 'success'})
    return jsonify({'status': 'failure'})
app.run(port=5000)
