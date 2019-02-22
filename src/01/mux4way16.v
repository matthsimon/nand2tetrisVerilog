`include "mux.v"
module mux4way16 (
    a, b, c, d,
    sel,
    out
);

input [15:0] a, b, c, d;
input [1:0] sel;
output [15:0] out;

wire [15:0] x, y;

mux mux1 [15:0] (a, b, sel[0], x);
mux mux2 [15:0] (c, d, sel[0], y);
mux mux3 [15:0] (x, y, sel[1], out);

endmodule
