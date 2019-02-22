COCOTB := $(PWD)/cocotb
SRC := $(PWD)/src
TESTDIRS := $(shell ls test)
COMPILE_ARGS := $(foreach d, $(TESTDIRS), -I$(SRC)/$d)
export

MODS :=
$(foreach d, $(TESTDIRS), $(eval include $(PWD)/test/$d/tests.mk))

all: $(MODS)

$(MODS):
	$(foreach d, $(TESTDIRS), cd test/$d && $(MAKE) $@ MODS=$@)

clean:
	@find . -name "obj" | xargs rm -rf
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*results.xml" | xargs rm -rf
	$(foreach d, $(TESTDIRS), cd test/$d && $(MAKE) clean)

