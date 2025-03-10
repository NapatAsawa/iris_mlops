install: 
	uv sync

train-model:
	uv run python model_train.py

local-run:
	uv run fastapi dev main.py

unit-test-run:
	uv run pytest test.py

docker-build:
	docker build -f Dockerfile -t iris-api .

docker-run: docker-build
	docker run -p 8000:80 iris-api
