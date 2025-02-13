echo "Upgrading pip..."
python3 -m pip install --upgrade pip

echo "Building project packages..."
python3 -m pip install -r requirements.txt
python3 -m pip install install sqlite-devel -y

echo "Migrating Database..."
python3 manage.py makemigrate --noinput
python3 manage.py migrate --noinput