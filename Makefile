
local-dev:
	docker run --rm -it -v $(PWD):/app \
		--workdir /app \
		rai-python-image bash

test:
	docker run --rm -it -v $(PWD):/src \
		--workdir /src \
		rai-python-image pytest