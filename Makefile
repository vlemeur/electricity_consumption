include influx_db_config.mk

run-all:
	@make run-influxdb

run-influxdb:
	@docker run -d -p 8086:8086 \
      -v $(INFLUXDB_PATH):/var/lib/influxdb2 \
	  --name electric-influxdb \
      -e DOCKER_INFLUXDB_INIT_MODE=$(DOCKER_INFLUXDB_INIT_MODE) \
      -e DOCKER_INFLUXDB_INIT_USERNAME=$(DOCKER_INFLUXDB_INIT_USERNAME) \
      -e DOCKER_INFLUXDB_INIT_PASSWORD=$(DOCKER_INFLUXDB_INIT_PASSWORD) \
      -e DOCKER_INFLUXDB_INIT_ORG=$(DOCKER_INFLUXDB_INIT_ORG) \
      -e DOCKER_INFLUXDB_INIT_BUCKET=$(DOCKER_INFLUXDB_INIT_BUCKET) \
      -e INFLUXDB_ADMIN_ENABLED=true \
      influxdb:2.0

clean-influxdb:
	@docker stop electric-influxdb || true && docker rm electric-influxdb || true

clean-all:
	@make clean-influxdb
