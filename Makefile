COCOTB := $(PWD)/cocotb
SRC := $(PWD)/src
TESTDIR := $(PWD)/test
COMPILE_ARGS := -I$(SRC)
export

MODS :=
include modules.mk

all: $(MODS)

$(MODS):
	cd $(TESTDIR) && $(MAKE) $@ MODS=$@

clean:
	@find . -name "obj" | xargs rm -rf
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*results.xml" | xargs rm -rf
	cd $(TESTDIR) && $(MAKE) clean

