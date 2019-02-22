`include "not.v"
module or8way (
    a,
    out
);

input [7:0] a;
output out;

wire [7:0] nota;

logical_not not8 [7:0] (a, nota);
assign out = ~&nota;

endmodule
