$(MODS): export VERILOG_SOURCES=$(SRC)/$(MODS).v
$(MODS): export TOPLEVEL=$(MODS)
$(MODS): export MODULE=$(MODS)_test
$(MODS): clean-vvp sim

not: export TOPLEVEL=logical_not

not16: export VERILOG_SOURCES += $(SRC)/not.v

and: export VERILOG_SOURCES += $(SRC)/not.v
and: export TOPLEVEL=logical_and

and16: export VERILOG_SOURCES += $(SRC)/and.v $(SRC)/not.v

or: export VERILOG_SOURCES += $(SRC)/not.v
or: export TOPLEVEL=logical_or

or16: export VERILOG_SOURCES += $(SRC)/not.v

xor: export VERILOG_SOURCES=$(SRC)/xor.v $(SRC)/not.v
xor: export TOPLEVEL=logical_xor

halfadder: export VERILOG_SOURCES += $(SRC)/xor.v $(SRC)/and.v $(SRC)/not.v

fulladder: export VERILOG_SOURCES += $(SRC)/xor.v $(SRC)/and.v $(SRC)/not.v
fulladder: export VERILOG_SOURCES += $(SRC)/halfadder.v $(SRC)/or.v

add16: export VERILOG_SOURCES += $(SRC)/xor.v $(SRC)/and.v $(SRC)/not.v
add16: export VERILOG_SOURCES += $(SRC)/halfadder.v $(SRC)/fulladder.v $(SRC)/or.v

mux: export VERILOG_SOURCES += $(SRC)/not.v

mux16: export VERILOG_SOURCES += $(SRC)/mux.v $(SRC)/not.v

mux4way16: export VERILOG_SOURCES += $(SRC)/mux.v $(SRC)/not.v

mux8way16: export VERILOG_SOURCES += $(SRC)/mux4way16.v $(SRC)/mux.v $(SRC)/not.v

inc16: export VERILOG_SOURCES += $(SRC)/xor.v $(SRC)/and16.v $(SRC)/and.v $(SRC)/not.v

alu: export VERILOG_SOURCES += $(SRC)/mux16.v $(SRC)/not16.v $(SRC)/mux.v $(SRC)/not.v
alu: export VERILOG_SOURCES += $(SRC)/add16.v $(SRC)/and16.v $(SRC)/and.v $(SRC)/or.v
alu: export VERILOG_SOURCES += $(SRC)/xor.v $(SRC)/halfadder.v $(SRC)/fulladder.v

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim

clean-vvp:
	$(RM) $(SIM_BUILD)/sim.vvp
