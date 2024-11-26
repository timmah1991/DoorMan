from flask import Flask, request, jsonify
from pyflipper.pyflipper import PyFlipper
import time

app = Flask(__name__)

flipper = PyFlipper(com="/dev/tty.usbmodemflip_Arull1n31")
resend_frequency = 0.02
resend_count = 5

@app.route('/sms', methods=['POST'])
def sms():
    message = request.form.get('Body', '').strip()
    if not "butthole" in message:
        return jsonify({"message": "gotta say the word"}), 400

    for i in range(resend_count):
        flipper.subghz.tx_from_file("/ext/subghz/Dearborn.sub")
        time.sleep(resend_frequency)

    return jsonify({"message": "opening the gates, sire"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
