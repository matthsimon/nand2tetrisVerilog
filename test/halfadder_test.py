'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def halfadder_test(dut, testdata):
    ''' Test Half Adder '''
    in_x, in_y, out, carry = testdata
    yield Timer(10000)
    dut.x = in_x
    dut.y = in_y
    yield Timer(10000)

    if dut.out.value != out or dut.carry.value != carry:
        raise cocotb.result.TestFailure(
            "Wrong result: HalfAdder(%d, %d) = (%d, %d) but got (%d, %d) instead"
            % (in_x, in_y, out, carry, dut.out.value, dut.carry.value))

TF = TestFactory(halfadder_test)
TF.add_option("testdata", [(0, 0, 0, 0),
                           (0, 1, 1, 0),
                           (1, 0, 1, 0),
                           (1, 1, 0, 1)])
TF.generate_tests()
