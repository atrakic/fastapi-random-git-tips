build:
	docker-compose up --build

test:
	python -m pytest tests

clean:
	docker-compose down -v
