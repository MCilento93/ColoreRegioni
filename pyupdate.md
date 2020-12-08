# update version
kind=['major','minor','patch']
bumpversion --current-version 0.1.0 patch setup.py setup.cfg

# generate wheel
python setup.py sdist bdist_wheel

# update pypi
twine upload --skip-existing dist/*

# (optional) testpypi
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*

# (info) PyPI
https://pypi.org/project/ColoreRegioni/#description
https://pypistats.org/packages/coloreregioni
