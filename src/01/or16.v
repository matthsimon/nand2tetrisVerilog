`include "or.v"
module or16 (
   input [15:0] a, b,
   output [15:0] out
);

logical_or orall [15:0] (a, b, out);

endmodule
