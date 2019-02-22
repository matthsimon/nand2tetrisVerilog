module logical_not (
    a,
    out
);

input a, out;

assign out = a ~& a;

endmodule
