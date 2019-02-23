`include "dmux4way.v"
module dmux8way (
    input inp,
    input [2:0] sel,
    output a, b, c, d, e, f, g, h
);

wire pick1, pick2;

dmux pick(inp, sel[2], pick1, pick2);
dmux4way dmux1(pick1, sel[1:0], a, b, c, d);
dmux4way dmux2(pick2, sel[1:0], e, f, g, h);

endmodule
