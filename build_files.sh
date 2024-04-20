echo "Building the project..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py
python3.10 -m pip install -r requirements.txt
python3.10 manage.py collectstatic