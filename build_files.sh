echo "Upgrading pip..."
python3 -m pip install --upgrade pip

echo "installing sqlite3"
sudo apt install libsqlite3-dev
pyenv install 3.11.3

echo "Building project packages..."
python3 -m pip install -r requirements.txt

echo "Migrating Database..."
python3 manage.py makemigrate --noinput
python3 manage.py migrate --noinput