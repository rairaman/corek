
local-dev:
	docker run --rm -it -v $(PWD):/app \
		--workdir /app \
		rai-python-image bash
