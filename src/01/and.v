`include "not.v"
module logical_and (
    a,
    b,
    out
);

input a, b;
output out;

wire a, b, out;

logical_not l_not(a ~& b, out);

endmodule
