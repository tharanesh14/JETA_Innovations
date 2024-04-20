echo "Building the project..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic