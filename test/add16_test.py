'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def add16_test(dut, testdata):
    ''' Test 16bit Adder '''
    x, y, out = testdata
    yield Timer(10000)
    dut.x = x
    dut.y = y
    yield Timer(10000)

    if dut.out.value != out:
        raise cocotb.result.TestFailure(
            "Wrong result: 0x%x + 0x%x = 0x%x but got 0x%x instead"
            % (x, y, out, dut.out.value))

TF = TestFactory(add16_test)
TF.add_option("testdata", [(0x0, 0x0, 0x0),
                           (0xFFFF, 0x0, 0xFFFF),
                           (0xFFFF, 0xFFFF, 0xFFFE),
                           (0x2222, 0x2222, 0x4444),
                           (0x0AFE, 0x0D12, 0x1810)])
TF.generate_tests()
