

'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer


@cocotb.coroutine
def or8way_test(dut, testdata):
    ''' Test OR8WAY gate '''
    in_a, out = testdata
    yield Timer(10000)
    dut.a = in_a
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: OR8WAY(0x%x) = 0x%x but got 0x%x instead"
            % (in_a, out, dut.out.value))

TF = TestFactory(or8way_test)
TF.add_option("testdata", [(0x0, 0),
                           (0x10, 1),
                           (0xFF, 1)])
TF.generate_tests()
