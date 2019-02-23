'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def mux4way16_test(dut, testdata):
    ''' Test MUX4WAY16'''
    in_a, in_b, in_c, in_d, sel, out = testdata
    yield Timer(10000)
    dut.a = in_a
    dut.b = in_b
    dut.c = in_c
    dut.d = in_d
    dut.sel = sel
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: MUX4WAY16(0x%x, 0x%x, 0x%x, 0x%x, %d) = 0x%x but got 0x%x instead"
            % (in_a, in_b, in_c, in_d, sel, out, dut.out.value))

TF = TestFactory(mux4way16_test)
TF.add_option("testdata", [(0x0, 0xBBBB, 0xCCCC, 0xDDDD, 0, 0x0),
                           (0xAAAA, 0xBBBB, 0xCCCC, 0xDDDD, 0, 0xAAAA),
                           (0xAAAA, 0xBBBB, 0xCCCC, 0xDDDD, 1, 0xBBBB),
                           (0xAAAA, 0xBBBB, 0xCCCC, 0xDDDD, 2, 0xCCCC),
                           (0xAAAA, 0xBBBB, 0xCCCC, 0xDDDD, 3, 0xDDDD)])
TF.generate_tests()
