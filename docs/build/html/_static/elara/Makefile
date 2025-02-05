build:
	python3 -m build

upload: build
	@if [ ! -f ~/.pypirc ] && [ -z "$$TWINE_PASSWORD" ]; then \
		echo "Error: PyPi credentials not found." ; \
		echo "Please create a ~/.pypirc file or set the TWINE_PASSWORD environment variable." ; \
		exit 1 ; \
	fi
	python3 -m twine upload dist/*

clean:
	rm -rf dist build *.egg-info