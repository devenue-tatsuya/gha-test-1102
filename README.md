## server 起動

cd server
flask run

## API に curl

curl -X POST localhost:5000/api/heroes -H "Content-Type: application/json" -d '{"name": {"userName": "太郎"}}'
