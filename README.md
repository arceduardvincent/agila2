## Deployment
1. Docker setup.
2. Heroku setup.

## Installation via pipenv
1. Install [pipenv](https://pypi.org/project/pipenv/)
2. Clone this repo and `cd agila`
3. Run `pip install --user --upgrade pipenv` to get the latest pipenv version.
4. Run `pipenv --python 3.7`
5. Run `pipenv install`


## Installation
1. Clone this repo and `cd agila`
2. Run `./bin/setup.sh` to get the latest pipenv version.
3. Run `source /usr/local/bin/virtualenvwrapper.sh`
4. Run `mkvirtualenv agila`
5. Run `workon agila`


## Getting Started
Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).
Browse to http://localhost:3000/

```
npm install
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata fixtures/roles.json
npm run dev
```



## Import fixtures order

```
python manage.py loaddata fixtures/roles.json
```

### Where you can find the API docs?
    http://localhost:8000/api-docs/

    
