#/bin/bash
source venv/bin/activate
python3 httpserver.py &
ngrok http --url=evolving-helped-newt.ngrok-free.app 5000 &
echo "server and forwarder running"