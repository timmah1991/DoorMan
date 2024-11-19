from flask import Flask, request, jsonify
import serial
import os

app = Flask(__name__)

# Serial device configuration
SERIAL_DEVICE = '/dev/serial/by-id/usb-Flipper_Devices_Inc._Flipper_Arull1n3_flip_Arull1n3-if00'  # Replace with your device path
BAUD_RATE = 230400  # Replace with your device's baud rate
TIMEOUT = 2  # Timeout for serial communication

# Command to send
BASE_COMMAND = "subghz tx_from_file /ext/subghz/Dearborn.sub 100 0\n"


def send_serial_command(command):
    """Send a command to the serial device and return the response."""
    try:
        with serial.Serial(SERIAL_DEVICE, BAUD_RATE, timeout=TIMEOUT) as ser:
            ser.write(command.encode('utf-8'))
            print(f"Sent command: {command.strip()}")
            
            # Read response if needed
            response = ser.read_until(b'\n').decode('utf-8').strip()
            print(f"Received response: {response}")
            return response
    except serial.SerialException as e:
        print(f"Error with serial communication: {e}")
        return str(e)


@app.route('/sms', methods=['POST'])
def sms():
    """
    Webhook to receive SMS messages and trigger serial commands.
    """
    # Get the incoming SMS body
    message = request.form.get('Body', '').strip()
    if not message:
        return jsonify({"error": "No SMS message received"}), 400

    # Optionally customize the command based on SMS content
    command = BASE_COMMAND  # Use BASE_COMMAND or modify based on `message`
    
    # Send the serial command
    response = send_serial_command(command)

    # Return response
    return jsonify({"message": "Command sent", "response": response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)