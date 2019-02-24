'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def fulladder_test(dut, testdata):
    ''' Test Full Adder '''
    x, y, z, out, carry = testdata
    yield Timer(10000)
    dut.x = x
    dut.y = y
    dut.z = z
    yield Timer(10000)

    if dut.out.value != out or dut.carry.value != carry:
        raise cocotb.result.TestFailure(
            "Wrong result: FullAdder(%d, %d, %d) = (%d, %d) but got (%d, %d) instead"
            % (x, y, z, out, carry, dut.out.value, dut.carry.value))

TF = TestFactory(fulladder_test)
TF.add_option("testdata", [(0, 0, 0, 0, 0),
                           (0, 0, 1, 1, 0),
                           (0, 1, 0, 1, 0),
                           (0, 1, 1, 0, 1),
                           (1, 0, 0, 1, 0),
                           (1, 0, 1, 0, 1),
                           (1, 1, 0, 0, 1),
                           (1, 1, 1, 1, 1)])
TF.generate_tests()
