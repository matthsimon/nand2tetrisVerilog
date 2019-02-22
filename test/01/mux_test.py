'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def mux_test(dut, testdata):
    ''' Test MUX'''
    in_a, in_b, sel, out = testdata
    yield Timer(10000)
    dut.a = in_a
    dut.b = in_b
    dut.sel = sel
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: MUX(%d, %d, %d) = %d but got %d instead"
            % (in_a, in_b, sel, out, dut.out.value))

TF = TestFactory(mux_test)
TF.add_option("testdata", [(0, 0, 0, 0),
                           (1, 0, 0, 1),
                           (1, 0, 1, 0),
                           (0, 1, 1, 1)])
TF.generate_tests()
