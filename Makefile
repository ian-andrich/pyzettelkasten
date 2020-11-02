.PHONY: env

env: env.yml .env

.env: env.yml
	conda env create -f env.yml || conda env update -f env.yml
	touch .env
