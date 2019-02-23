'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def dmux_test(dut, testdata):
    ''' Test DMUX'''
    inp, sel, out_a, out_b = testdata
    yield Timer(10000)

    dut.inp = inp
    dut.sel = sel
    yield Timer(10000)

    if dut.a.value != out_a or dut.b.value != out_b:
        raise cocotb.result.TestFailure(
            "Wrong result: DMUX(%d, %d) = (%d, %d) but got (%d, %d) instead"
            % (inp, sel, out_a, out_b, dut.a.value, dut.b.value))

TF = TestFactory(dmux_test)
TF.add_option("testdata", [(0, 0, 0, 0),
                           (1, 0, 1, 0),
                           (0, 1, 0, 0),
                           (1, 1, 0, 1)])
TF.generate_tests()
