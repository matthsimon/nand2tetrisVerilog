module logical_or (
    input a, b,
    output out
);

wire na, nb;

logical_not lnota(a, na);
logical_not lnotb(b, nb);
assign out = na ~& nb;

endmodule
