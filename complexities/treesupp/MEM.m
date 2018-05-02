function [commd,rule,num,numnodes,depths,t_l,t_r] = MEM(forms,operands)

if nargin < 3 num = ''; end

% Construct left (form) and right (rule) trees
[t_l] = constructTree(forms,'FORM');
[t_r] = constructTree(operands,'MEM');

% Concatonate left and right trees
[commd rule] = linkLeftRightExpressions(t_l,t_r,'<-');

% Calculate complexity
numnodes = nnodes(t_l) - (depth(t_l)>0) + nnodes(t_r) + 1 - (depth(t_r)>0);
depths = [depth(t_l) depth(t_r)];




