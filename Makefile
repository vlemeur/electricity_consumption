INFLUXDB_PATH := "/Users/vincentlemeur/Dropbox/Vincent/Work & Science/Databases/electric"
DOCKER_INFLUXDB_INIT_MODE := "setup"
DOCKER_INFLUXDB_INIT_USERNAME := "my-user"
DOCKER_INFLUXDB_INIT_PASSWORD := "my-password"
DOCKER_INFLUXDB_INIT_ORG := "my-org"
DOCKER_INFLUXDB_INIT_BUCKET := "my-bucket"

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
      influxdb:2.0

clean-influxdb:
	@docker stop electric-influxdb || true && docker rm electric-influxdb || true

clean-all:
	@make clean-influxdb
