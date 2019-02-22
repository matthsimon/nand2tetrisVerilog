
'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def mux16_test(dut, testdata):
    ''' Test MUX16'''
    in_a, in_b, sel, out = testdata
    yield Timer(10000)
    dut.a = in_a
    dut.b = in_b
    dut.sel = sel
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: MUX(0x%x, 0x%x, %d) = 0x%x but got 0x%x instead"
            % (in_a, in_b, sel, out, dut.out.value))

TF = TestFactory(mux16_test)
TF.add_option("testdata", [(0x0, 0xBBBB, 0, 0x0),
                           (0xAAAA, 0xBBBB, 0, 0xAAAA),
                           (0xAAAA, 0x0, 1, 0x0),
                           (0xAAAA, 0xBBBB, 1, 0xBBBB)])
TF.generate_tests()
