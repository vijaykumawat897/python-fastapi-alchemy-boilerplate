CONTRACT=contracts/openapi.yaml
MODELS=app/generated/models.py

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

generate:
	datamodel-codegen --input $(CONTRACT) --input-file-type openapi --output $(MODELS)

run:
	uvicorn app.main:app --reload

test:
	pytest

clean:
	rm -rf $(MODELS)

revision:
	@if [ -z "$(m)" ]; then \
		echo "❌ Usage: make revision m=\"migration message\""; \
		exit 1; \
	fi
	alembic revision --autogenerate -m "$(m)"

upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade -1

migrate: upgrade