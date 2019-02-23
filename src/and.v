module logical_and (
    input a, b,
    output out
);

logical_not l_not(a ~& b, out);

endmodule
