`include "not.v"
module logical_xor (
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
assign out = (a ~& nb) ~& (na ~& b);

endmodule
