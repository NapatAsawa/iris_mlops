docker-build:
	docker build -f Dockerfile -t iris-api .

docker-run: docker-build
	docker run -p 8000:80 iris-api
