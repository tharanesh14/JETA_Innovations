echo "Building the project..."
# python3.9 -c 'import sys; print("Python Runtime Version:", sys.version)'
# Download and install pip
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3.9 get-pip.py

# Install project dependencies
pip install -r requirements.txt

# Print Python runtime version
# python_version=$(python3 -c 'import sys; print(sys.version)')
# echo "Python Runtime Version: $python_version"

# Run Django collectstatic command or any other build commands
python3.9 manage.py collectstatic

# Run other build commands as needed
