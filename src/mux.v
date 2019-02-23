`include "not.v"
module mux (
    input a, b, sel,
    output out
);

wire nsel;

logical_not lnot(sel, nsel);
assign out = (a ~& nsel) ~& (b ~& sel);

endmodule
