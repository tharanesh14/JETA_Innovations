echo "BUILD START"
pip install Django
pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py collectstatic
echo "BUILD END"