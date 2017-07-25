build:
	docker build -t flask-sample-one:latest .

run:
	docker run -d -p 5000:5000 flask-sample-one