'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
def not_test(dut):
    '''
    Test NOT gate
    '''
    yield Timer(10000)
    dut.a = 0
    yield Timer(10000)
    if not dut.out.value:
        raise cocotb.result.TestFailure

    dut.a = 1
    yield Timer(10000)
    if dut.out.value:
        raise cocotb.result.TestFailure
