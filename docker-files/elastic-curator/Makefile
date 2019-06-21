include ../../util/common.mk

PROGNAME = elastic_curator

image:
	docker build -t $(PROGNAME) -f Dockerfile .

publish: image publish-no-deps

publish-no-deps:
	$(call docker_push_images,$(PROGNAME))
