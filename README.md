Coin API
=============
Backend API for the project called Coding-In.

1. Install Docker Desktop
2. Run this command
~~~ bash
git clone https://github.com/inourbubble2/coin-backend.git
cd coin-backend
docker-compose up -d --build
~~~
3. Check http://0.0.0.0:5000/api/

If you need migration, run
~~~ bash
docker exec -it coin-backend alembic upgrade head
~~~
