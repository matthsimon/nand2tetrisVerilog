$(MODS): export VERILOG_SOURCES=$(SRC)/$(MODS).v
$(MODS): export TOPLEVEL=$(MODS)
$(MODS): export MODULE=$(MODS)_test
$(MODS): clean-vvp sim

not: export VERILOG_SOURCES=$(SRC)/not.v
not: export TOPLEVEL=logical_not

and: export VERILOG_SOURCES=$(SRC)/and.v $(SRC)/not.v
and: export TOPLEVEL=logical_and

and16: export VERILOG_SOURCES += $(SRC)/not.v

or: export VERILOG_SOURCES=$(SRC)/or.v
or: export TOPLEVEL=logical_or

xor: export VERILOG_SOURCES=$(SRC)/xor.v $(SRC)/not.v
xor: export TOPLEVEL=logical_xor

halfadder: export VERILOG_SOURCES += $(SRC)/xor.v $(SRC)/and.v $(SRC)/not.v

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim

clean-vvp:
	$(RM) $(SIM_BUILD)/sim.vvp
