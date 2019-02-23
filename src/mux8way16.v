`include "mux4way16.v"
module mux8way16 (
    input [15:0] a, b, c, d, e, f, g, h,
    input [2:0] sel,
    output [15:0] out
);

wire [15:0] x, y;

mux4way16 mux1(a, b, c, d, sel[1:0], x);
mux4way16 mux2(e, f, g, h, sel[1:0], y);
mux mux3 [15:0] (x, y, sel[2], out);

endmodule
