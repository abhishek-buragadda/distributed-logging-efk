include ../util/common.mk

#assignment done to avoid re-evaluation, that is used in subsequent target
BUILD_DATE := ${BUILD_DATE}
SUBDIRS := elasticsearch elastic-curator elastic-indices-check elastic-readiness-check fluentd fluentd-ds fluentd-ds-aggr

all build test clean docs linux: nothing

image publish publish-no-deps: $(SUBDIRS)

nothing:
	@echo > /dev/null

$(SUBDIRS):
	@echo "Make $(MAKECMDGOALS) in $@"
	@$(MAKE) -C $@ $(MAKECMDGOALS) BUILD_DATE=$(BUILD_DATE)

.PHONY: all build clean docs image publish publish-no-deps test $(SUBDIRS)
