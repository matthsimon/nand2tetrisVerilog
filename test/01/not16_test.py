'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
def not16_test(dut):
    '''
    Test NOT16 gate
    '''
    yield Timer(10000)
    dut.a = 0xA0A0
    yield Timer(10000)
    if  dut.out.value != 0x5F5F:
        raise cocotb.result.TestFailure

    dut.a = dut.out.value
    yield Timer(10000)
    if dut.out.value != 0xA0A0:
        raise cocotb.result.TestFailure
