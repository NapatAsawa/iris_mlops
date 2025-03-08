docker-build:
	docker build -f Dockerfile -t iris-api .

docker-run: docker-build
	docker run -p 8000:80 iris-api

fastapp-run:
	uv run fastapi dev main.py

train-model:
	uv run python train.py

unit-test-run:
	uv run pytest test.py