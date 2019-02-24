module add16 (
    input [15:0] x, y,
    output [15:0] out
);

wire [15:0] carry;

halfadder ha(x[0], y[0], out[0], carry[0]);
fulladder fa[14:0] (x[15:1], y[15:1], carry[14:0], out[15:1], carry[15:1]);

endmodule
