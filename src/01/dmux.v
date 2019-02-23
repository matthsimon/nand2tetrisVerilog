`include "not.v"
module dmux (
    input inp, sel,
    output a, b
);

wire nsel;

logical_not lnot(sel, nsel);
logical_not lnota(nsel ~& inp, a);
logical_not lnotb(sel ~& inp, b);

endmodule
