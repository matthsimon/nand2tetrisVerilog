'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def dmux8way_test(dut, testdata):
    ''' Test DMUX8WAY'''
    inp, sel, expects = testdata
    yield Timer(10000)

    dut.inp = inp
    dut.sel = sel
    yield Timer(10000)

    outputs = (dut.a.value, dut.b.value, dut.c.value, dut.d.value,
               dut.e.value, dut.f.value, dut.g.value, dut.h.value)
    if outputs != expects:
        raise cocotb.result.TestFailure(
            "Wrong result: DMUX(%d, %d) = %s but got %s instead"
            % (inp, sel, expects, outputs))

TF = TestFactory(dmux8way_test)
TF.add_option("testdata", [(0, 0, (0, 0, 0, 0, 0, 0, 0, 0)),
                           (1, 0, (1, 0, 0, 0, 0, 0, 0, 0)),
                           (1, 1, (0, 1, 0, 0, 0, 0, 0, 0)),
                           (1, 2, (0, 0, 1, 0, 0, 0, 0, 0)),
                           (1, 3, (0, 0, 0, 1, 0, 0, 0, 0)),
                           (1, 4, (0, 0, 0, 0, 1, 0, 0, 0)),
                           (1, 5, (0, 0, 0, 0, 0, 1, 0, 0)),
                           (1, 6, (0, 0, 0, 0, 0, 0, 1, 0)),
                           (1, 7, (0, 0, 0, 0, 0, 0, 0, 1))])
TF.generate_tests()
