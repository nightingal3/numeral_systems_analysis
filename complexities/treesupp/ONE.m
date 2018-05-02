function [commd,rule,num,numnodes,depths,t_l,t_r] = ONE(form,numexp)

num = numexp;

% Construct left (form) and right (rule) trees
[t_l] = constructTree(form,'FORM');
[t_r] = constructTree('PRM','ONE');

% Concatonate left and right trees
[commd rule] = linkLeftRightExpressions(t_l,t_r,'=');

% Calculate complexity
numnodes = nnodes(t_l) -(depth(t_l)>0) + nnodes(t_r) + 1;
depths = [depth(t_l) depth(t_r)];




