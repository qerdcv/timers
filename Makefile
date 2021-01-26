COMPOSE ?= docker-compose -f compose-base.yml

.default: run
.EXPORT_ALL_VARIABLES:

build:
	$(COMPOSE) build

run: build
run:
	$(COMPOSE) up -d

remove-compose:
	$(COMPOSE) rm -f

#logs:
#	$(COMPOSE)