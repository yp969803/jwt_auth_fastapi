```
# create environment [ windows, linux, mac ]
python -m venv env

# activate environment [ windows ]
env/Scripts/activate

# activate environment [ linux & mac ]
source env/bin/activate

touch requirements.txt
```
```
requirements.txt :
fastapi==0.88.0
bcrypt==4.0.1
pyjwt==2.6.0
alembic>=1.9.1
uvicorn==0.20.0
SQLAlchemy>=1.4,<=2.0
psycopg2-binary==2.9.5
email-validator>=1.0.3
```

```
pip install -r requirements.txt

alembic revision --autogenerate -m "Create user model"


alembic/versions/some_sha_value_create_user_table.py
# kindly use the appropriate sha value as yours will be different from mine


alembic upgrade sha_value

uvicorn --reload main:app

```