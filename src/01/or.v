`include "not.v"
module logical_or (
    a,
    b,
    out
);

input a, b;
output out;

wire a, b, out;
wire na, nb;

logical_not lnota(a, na);
logical_not lnotb(b, nb);
assign out = na ~& nb;

endmodule
