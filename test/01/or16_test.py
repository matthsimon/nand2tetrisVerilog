
'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer


@cocotb.coroutine
def or16_test(dut, testdata):
    ''' Test OR16 gate '''
    in_a, in_b, out = testdata
    yield Timer(10000)
    dut.a = in_a
    dut.b = in_b
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: OR16(0x%x, 0x%x) = 0x%x but got 0x%x instead"
            % (in_a, in_b, out, dut.out.value))

TF = TestFactory(or16_test)
TF.add_option("testdata", [(0xA5A5, 0x5A5A, 0xFFFF),
                           (0xAAAA, 0xF, 0xAAAF),
                           (0xF, 0x1111, 0x111F),
                           (0xF0FF, 0xFFF0, 0xFFFF)])
TF.generate_tests()
