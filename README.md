# APIs-with-FastAPI

This is the documentation for the course Building APIs with FastAPI

Here you will find:
- The source code of the API
- The dockerfile
- The postman collection to test the API

#### First install venv globally
pip install python3.8-venv

#### Create virtual environment within working directory
python -m venv venv

#### Enter virtual environment
source venv/bin/activate

#### Install python fastapi, uvicorn
pip install fastapi uvicorn

#### Freeze all dependent packages
pip freeze > requirements.txt

#### Install requirements into venv (To rebuild env)
pip install -r requirements.txt


#### Install psycopg2-binary
pip install psycopg2-binary

#### Postgres Backend Test
import psycopg2

#### Example use case for postgres python client
url = "postgres://batch_user:xxxx@localhost:5432/postgres" 
connection = psycopg2.connect(url)
cursor = connection.cursor()

cursor.execute("SELECT version();")
version = cursor.fetchone()
print(version)

connection.close()


#### Docker run Command to talk to DB
docker run -d --network=host \
	-e "DB_NAME="postgres" \
	-e "DB_PORT=5432" \
	-e "DB_USER=batch_user" \
	-e "DB_PASS="" \
	-e "DB_HOST=127.0.0.1" \
	--name some_name foo/bar

#### Running FastAPI using uvicorn

From within the python virtual environment run:

uvicorn app.main:app --reload
