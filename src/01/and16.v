`include "and.v"
module and16 (
   a,
   b,
   out
);

input [15:0] a, b;
output [15:0] out;

logical_and andall [15:0] (a, b, out);

endmodule