echo "Building the project..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
python -m pip install -r requirements.txt
python manage.py collectstatic