function [commd,rule,num,numnodes,depths,t_l,t_r] = GAU(form,operand,numexp)

num = numexp;

% Construct left (form) and right (rule) trees
[t_l] = constructTree(form,'FORM');
[t_r] = constructTree(operand,'GAU');

% Concatonate left and right trees
[commd rule] = linkLeftRightExpressions(t_l,t_r,'=');

% Calculate complexity
%numnodes = nnodes(t_l) + nnodes(t_r) + 1;
numnodes = nnodes(t_l) + nnodes(t_r); % G(x) -> x where x is floating
depths = [depth(t_l) depth(t_r)];




