echo "Building the project..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
echo "Building the cmake..."
python3.9 -m pip uninstall cmake
python3.9 -m pip uninstall dlib
python3.9 -m pip install cmake
python3.9 -m pip install dlib
echo "Building the cmake..."
python3.9 -m cmake --version
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic