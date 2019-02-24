module fulladder (
    input x, y, z,
    output out, carry
);

wire xy, xyc, zc;

halfadder ha1(x, y, xy, xyc);
halfadder ha2(xy, z, out, zc);
logical_or finalcarry(xyc, zc, carry);

endmodule
