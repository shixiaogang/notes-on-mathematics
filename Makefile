.PHONY: test build volume volumes all watch release clean check-target

test:
	./tests/check-index-terms.sh
	python3 -m unittest -v tests/test_target_pdfs.py
	bash tests/check-build-clean.sh
	bash tests/check-part-openings.sh
	bash tests/check-paragraph-statements.sh

build:
	./build.sh build

volume:
	./build.sh volume $(VOLUME)

volumes:
	./build.sh volumes

all:
	./build.sh all

watch:
	./build.sh watch $(VOLUME)

release:
	./build.sh release $(VOLUME)

clean:
	./build.sh clean

check-target:
	./build.sh check-target
