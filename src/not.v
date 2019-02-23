module logical_not (
    input a,
    output out
);

assign out = a ~& a;

endmodule
