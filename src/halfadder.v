module halfadder (
    input x, y,
    output out, carry
);

logical_xor lxor(x, y, out);
logical_and land(x, y, carry);

endmodule
