COMPOSE=docker compose

#  init containers (postgres, migrate, rabbitmq) and start scraping
a:
	cd magalu && poetry run python main.py

# open repository in browser
or:
	open https://github.com/guimassoqueto/scrap-magalu

# create .env from .env.sample
env:
	cp .env.sample .env


