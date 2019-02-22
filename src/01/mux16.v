`include "mux.v"
module mux16 (
    a,
    b,
    sel,
    out
);

input [15:0] a, b;
input sel;
output [15:0] out;

mux mux16 [15:0] (a, b, sel, out);

endmodule