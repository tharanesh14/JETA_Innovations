echo "Building the project..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10.12 get-pip.py
python3.10.12 -m pip install -r requirements.txt
python3.10.12 manage.py collectstatic