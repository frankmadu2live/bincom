set -0 effexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate 