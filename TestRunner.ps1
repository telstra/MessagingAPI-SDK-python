python -m venv tdev  

tdev\\Scripts\\activate

pip install six python-dateutil urllib3 certifi

python -m unittest discover test

deactivate tdev

rm -r tdev