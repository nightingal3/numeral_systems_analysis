function [expression] = linkTreeNodes(t,opt)
% Wrapper function to recursively traverse tree and obtain expression

% Recursion top-down: combined expression = parent ( child_l child_r )
expression = recursiveExpression(t,opt);

end