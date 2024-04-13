echo "BUILD START"
# pip3 --version
# python3.9 pip install Django
python3.10 pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
python3.10 manage.py collectstatic
echo "BUILD END"