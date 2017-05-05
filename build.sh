PYTHONPATH=''
nosetests --with-xunit --all-modules --traverse-namespace --with-coverage --cover-package=./unnecessary_math --cover-inclusive
python -m coverage xml --include=unnecessary_math*
pylint -f parseable -d I0011,R0801 ./unnecessary_math | tee pylint.out
