'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def inc16_test(dut, testdata):
    ''' Test Inc16 '''
    x, out = testdata
    yield Timer(10000)
    dut.x = x
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: Inc16(%d) = %d but got %d instead"
            % (x, out, dut.out.value))

TF = TestFactory(inc16_test)
TF.add_option("testdata", [(0x0, 0x1),
                           (0xF, 0x10),
                           (0xFFFF, 0x0),
                           (0xAB1, 0xAB2),
                           (0xAB3, 0xAB4)])
TF.generate_tests()
