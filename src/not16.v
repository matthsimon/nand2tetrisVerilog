module not16 (
   input [15:0] a,
   output [15:0] out
);

logical_not notall [15:0] (a, out);

endmodule
