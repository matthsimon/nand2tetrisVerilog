
'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer


@cocotb.coroutine
def and16_test(dut, testdata):
    ''' Test AND16 gate '''
    in_a, in_b, out = testdata
    yield Timer(10000)
    dut.a = in_a
    dut.b = in_b
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: AND(0x%x, 0x%x) = 0x%x but got 0x%x instead"
            % (in_a, in_b, out, dut.out.value))

TF = TestFactory(and16_test)
TF.add_option("testdata", [(0xA5A5, 0x5A5A, 0x0),
                           (0xAAAA, 0xF, 0xA),
                           (0xF, 0x1111, 0x1),
                           (0xF0FF, 0xFFF0, 0xF0F0)])
TF.generate_tests()
