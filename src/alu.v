module alu (
    input [15:0] x, y,
    input zx, nx, zy, ny, f, no,
    output [15:0] out,
    output zr, ng
);

wire [15:0] xorzero, notx, opx, yorzero, noty, opy, andxy, addxy, result, notout;

mux16 pickzerox(x, 16'b0, zx, xorzero);
not16 negatex(xorzero, notx);
mux16 picknotx(xorzero, notx, nx, opx);

mux16 pickzeroy(y, 16'b0, zy, yorzero);
not16 negatey(yorzero, noty);
mux16 picknoty(yorzero, noty, ny, opy);

and16 andop(opx, opy, andxy);
add16 addop(opx, opy, addxy);

mux16 operation(andxy, addxy, f, result);
logical_xor pickresult [15:0] (result, no, out);

not16 negateout(out, notout);
logical_not iszero(~&notout, zr);
assign ng = out[15];

endmodule
