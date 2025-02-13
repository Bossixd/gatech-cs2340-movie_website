echo "Building project packages..."
python3 -m pip install -r requirements.txt

echo "Migrating Database..."
python3 manage.py makemigrate --noinput
python3 manage.py migrate --noinput