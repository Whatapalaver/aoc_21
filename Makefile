build:
	docker build -t py_docker_aoc:dev --rm .

# builds container and opens shell
run: build
	docker run --rm -it --name py_docker_aoc_app \
		--env-file=.env \
		-v $(CURDIR):/app \
		py_aoc:dev

# Get additional shell in the running container by `make run`
shell:
	docker exec -it py_aoc_docker_app bash