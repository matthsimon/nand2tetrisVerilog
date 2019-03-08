module inc16(
    input [15:0] x,
    output [15:0] out
);

wire [16:0] carry;

assign carry[0] = 1;
logical_xor xor16 [15:0] (x, carry[15:0], out);
and16 carries(x, carry[15:0], carry[16:1]);

endmodule
