echo "Upgrading pip..."
pip install --upgrade pip >/dev/null
echo "Installing the wheel module..."
pip install wheel >/dev/null
echo "Building the module..."
python setup.py sdist bdist_wheel bdist_egg >/dev/null
echo "Installing the module..."
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl >/dev/null
echo "Done."
