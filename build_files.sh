echo "Building the project..."

# Download and install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

# Install project dependencies
python -m pip install -r requirements.txt

# Print Python runtime version
python_version=$(python3 -c 'import sys; print(sys.version)')
echo "Python Runtime Version: $python_version"

# Run Django collectstatic command or any other build commands
python manage.py collectstatic

# Run other build commands as needed
