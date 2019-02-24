# IOT_ADRINI
IOT PLATFORM ALL BOARD

## Installing

## Environment File
Create New Environment File save to .env or move .env.example 
```
mv .env.example .env
```
Value Environment File
```
### APP SETUP
APP_NAME = IOT_ADRINI
APP_HOST = 127.0.0.1
APP_PORT = 6969
SECRET_KEY = asdsagdasgdasf@asfdasgvdasda@#!@#!%$#%@#@@##
MEMCACHE_HOST=127.0.0.1
MEMCACHE_PORT=11211
FLASK_DEBUG = True

### REDIS SETUP
FLASK_REDIS_URL = redis://:pass@127.0.0.1:6379/0

### JWT SETUP
JWT_SECRET_KEY = wqertyudfgfhjhkcxvbnmn@123$32213

### DATABASE SETUP
DB_NAME = knotdb
DB_HOST = localhost
DB_PORT = 26257
DB_USER = root
DB_SSL = disable

#### DOCS

SWAGGER_URL = '/api/docs'
SWAGGER_API_URL = 'http://127.0.0.1:6968/static/swagger.json'

```

## Installing
At the time  only support Python3 or newer.

``` bash
pip3 install -r requirements.txt
```

After Installing Requirement File, Next Install redis

Fedora Based
``` bash
dnf install redis redis-cli
```

Debian based
``` bash
apt-get install redis redis-cli
```

Setup Your Redis auth see your .env file And Then

``` bash
redis-cli
127.0.0.1:6379> CONFIG SET requirepass "pass"

```

Runing Server
``` bash
sudo python manage.py server
```

Installing CockroachDB Reference [action](https://www.cockroachlabs.com/docs/stable/)

## Dockerize Development