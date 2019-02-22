`include "dmux.v"
module dmux4way (
    inp,
    sel,
    a, b, c, d
);

input inp;
input [1:0] sel;
output a, b, c, d;

wire pick1, pick2;

dmux selector(inp, sel[1], pick1, pick2);
dmux dmux1(pick1, sel[0], a, b);
dmux dmux2(pick2, sel[0], c, d);

endmodule
