# echo "BUILD START"
python3 -m pip install Django
python3 -m pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
python3 manage.py collectstatic
# echo "BUILD END"