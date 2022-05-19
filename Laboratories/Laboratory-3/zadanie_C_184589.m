clc
clear all
close all

load zadB_184589.mat
d = 0.85;
M = sparse(I - d*B*A);
r = M\b;
save zadC_184589 r