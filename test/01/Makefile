$(MODS): export VERILOG_SOURCES=$(SRC)/01/$(MODS).v
$(MODS): export TOPLEVEL=$(MODS)
$(MODS): export MODULE=$(MODS)_test
$(MODS): clean-vvp sim

not: export VERILOG_SOURCES=$(SRC)/01/not.v
not: export TOPLEVEL=logical_not
not: export MODULE=not_test
not: clean-vvp sim

and: export VERILOG_SOURCES=$(SRC)/01/and.v
and: export TOPLEVEL=logical_and
and: export MODULE=and_test
and: clean-vvp sim

or: export VERILOG_SOURCES=$(SRC)/01/or.v
or: export TOPLEVEL=logical_or
or: export MODULE=or_test
or: clean-vvp sim

xor: export VERILOG_SOURCES=$(SRC)/01/xor.v
xor: export TOPLEVEL=logical_xor
xor: export MODULE=xor_test
xor: clean-vvp sim

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim

clean-vvp:
	$(RM) $(SIM_BUILD)/sim.vvp
