function [commd,rule,num,numnodes,depths,t_l,t_r] = HIG(forms,numexp)

num = numexp;

% Construct left (form) and right (rule) trees
[t_l] = constructTree(forms{2},'FORM');
[t_r] = constructTree(forms{1},'HIG');

% Concatonate left and right trees
[commd rule] = linkLeftRightExpressions(t_l,t_r,'=');

% Calculate complexity
numnodes = nnodes(t_l) + nnodes(t_r) + 1;
depths = [depth(t_l) depth(t_r)];


end

