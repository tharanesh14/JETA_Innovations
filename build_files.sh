echo "BUILD START"
# pip3 --version
pip install -r requirements.txt
# python3 pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
python3 manage.py collectstatic
echo "BUILD END"