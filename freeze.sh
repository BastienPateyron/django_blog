source .venv_django2.2/bin/activate
pip freeze | grep -v "pkg-resources" > requirements.txt
