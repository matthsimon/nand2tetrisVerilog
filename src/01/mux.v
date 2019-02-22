`include "not.v"
module mux (
    a,
    b,
    sel,
    out
);

input a, b;
input sel;
output out;

wire nsel;

logical_not lnot(sel, nsel);
assign out = (a ~& nsel) ~& (b ~& sel);

endmodule
