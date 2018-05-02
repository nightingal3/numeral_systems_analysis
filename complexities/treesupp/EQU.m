function [commd,rule,num,numnodes,depths,t_l,t_r] = EQU(operand1,operand2,num)

if nargin < 3 num = ''; end

% Construct left (form) and right (rule) trees
[t_l] = constructTree(operand1,'EQU');
[t_r] = constructTree(operand2,'EQU');

% Concatonate left and right trees
[commd rule] = linkLeftRightExpressions(t_l,t_r,'<->');

% Calculate complexity
numnodes = nnodes(t_l) + nnodes(t_r) + 1;
depths = [depth(t_l) depth(t_r)];

