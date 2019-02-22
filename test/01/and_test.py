'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer


@cocotb.coroutine
def and_test(dut, testdata):
    ''' Test AND gate '''
    in_a, in_b, out = testdata
    yield Timer(10000)
    dut.a = in_a
    dut.b = in_b
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: AND(%d, %d) = %d but got %d instead"
            % (in_a, in_b, out, dut.out.value))

TF = TestFactory(and_test)
TF.add_option("testdata", [(0, 0, 0),
                           (0, 1, 0),
                           (1, 0, 0),
                           (1, 1, 1)])
TF.generate_tests()
