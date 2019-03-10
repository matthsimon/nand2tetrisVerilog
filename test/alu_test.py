'''
Author: Matthieu Simon
'''
import cocotb
from cocotb.regression import TestFactory
from cocotb.triggers import Timer

@cocotb.coroutine
def alu_test(dut, testdata):
    ''' Test ALU '''
    x, y, zx, nx, zy, ny, f, no, out, zr, ng = testdata
    yield Timer(10000)
    dut.x = x
    dut.y = y
    dut.zx = zx
    dut.zy = zy
    dut.nx = nx
    dut.ny = ny
    dut.f = f
    dut.no = no
    yield Timer(10000)

    if dut.out.value != out or dut.zr.value != zr or dut.ng.value != ng:
        raise cocotb.result.TestFailure(
            ("Wrong result: ALU(0x%x, 0x%x, %d, %d, %d, %d, %d, %d) ="
             + " (0x%x, %d, %d) but got (0x%x, %d, %d) instead result=0x%x")
            % (x, y, zx, nx, zy, ny, f, no, out, zr, ng,
               dut.out.value, dut.zr.value, dut.ng.value, dut.result.value))

TF = TestFactory(alu_test)
TF.add_option("testdata", [
    (0x0, 0xFFFF, 1, 0, 1, 0, 1, 0, 0x0, 1, 0),
    (0x0, 0xFFFF, 1, 1, 1, 1, 1, 1, 0x1, 0, 0),
    (0x0, 0xFFFF, 1, 1, 1, 0, 1, 0, 0xFFFF, 0, 1),
    (0x0, 0xFFFF, 0, 0, 1, 1, 0, 0, 0x0, 1, 0),
    (0x0, 0xFFFF, 1, 1, 0, 0, 0, 0, 0xFFFF, 0, 1),
    (0x0, 0xFFFF, 0, 0, 1, 1, 0, 1, 0xFFFF, 0, 1),
    (0x0, 0xFFFF, 1, 1, 0, 0, 0, 1, 0x0, 1, 0),
    (0x0, 0xFFFF, 0, 0, 1, 1, 1, 1, 0x0, 1, 0),
    (0x0, 0xFFFF, 1, 1, 0, 0, 1, 1, 0x1, 0, 0),
    (0x0, 0xFFFF, 0, 1, 1, 1, 1, 1, 0x1, 0, 0),
    (0x0, 0xFFFF, 1, 1, 0, 1, 1, 1, 0x0, 1, 0),
    (0x0, 0xFFFF, 0, 0, 1, 1, 1, 0, 0xFFFF, 0, 1),
    (0x0, 0xFFFF, 1, 1, 0, 0, 1, 0, 0xFFFE, 0, 1),
    (0x0, 0xFFFF, 0, 0, 0, 0, 1, 0, 0xFFFF, 0, 1),
    (0x0, 0xFFFF, 0, 1, 0, 0, 1, 1, 0x1, 0, 0),
    (0x0, 0xFFFF, 0, 0, 0, 1, 1, 1, 0xFFFF, 0, 1),
    (0x0, 0xFFFF, 0, 0, 0, 0, 0, 0, 0x0, 1, 0),
    (0x0, 0xFFFF, 0, 1, 0, 1, 0, 1, 0xFFFF, 0, 1),
    (0x11, 0x3, 1, 0, 1, 0, 1, 0, 0x0, 1, 0),
    (0x11, 0x3, 1, 1, 1, 1, 1, 1, 0x1, 0, 0),
    (0x11, 0x3, 1, 1, 1, 0, 1, 0, 0xFFFF, 0, 1),
    (0x11, 0x3, 0, 0, 1, 1, 0, 0, 0x11, 0, 0),
    (0x11, 0x3, 1, 1, 0, 0, 0, 0, 0x3, 0, 0),
    (0x11, 0x3, 0, 0, 1, 1, 0, 1, 0xFFEE, 0, 1),
    (0x11, 0x3, 1, 1, 0, 0, 0, 1, 0xFFFC, 0, 1),
    (0x11, 0x3, 0, 0, 1, 1, 1, 1, 0xFFEF, 0, 1),
    (0x11, 0x3, 1, 1, 0, 0, 1, 1, 0xFFFD, 0, 1),
    (0x11, 0x3, 0, 1, 1, 1, 1, 1, 0x12, 0, 0),
    (0x11, 0x3, 1, 1, 0, 1, 1, 1, 0x4, 0, 0),
    (0x11, 0x3, 0, 0, 1, 1, 1, 0, 0x10, 0, 0),
    (0x11, 0x3, 1, 1, 0, 0, 1, 0, 0x2, 0, 0),
    (0x11, 0x3, 0, 0, 0, 0, 1, 0, 0x14, 0, 0),
    (0x11, 0x3, 0, 1, 0, 0, 1, 1, 0xE, 0, 0),
    (0x11, 0x3, 0, 0, 0, 1, 1, 1, 0xFFF2, 0, 1),
    (0x11, 0x3, 0, 0, 0, 0, 0, 0, 0x1, 0, 0),
    (0x11, 0x3, 0, 1, 0, 1, 0, 1, 0x13, 0, 0)])
TF.generate_tests()
