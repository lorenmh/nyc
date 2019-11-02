.PHONY: freeze
freeze:
	source venv/bin/activate && \
		pip freeze > requirements.txt

.PHONY: install
install:
	source venv/bin/activate && \
		pip install -r requirements.txt

.PHONY: run
run:
	source venv/bin/activate && \
	source ./secrets.sh && \
		FLASK_APP=app.py flask run
