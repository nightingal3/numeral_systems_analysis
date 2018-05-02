function [commd rule] = linkLeftRightExpressions(t_l,t_r,linksymbol)

commd = [recursiveExpression(t_l,'command',0),' ',linksymbol,' ',recursiveExpression(t_r,'command',1)];
rule = [recursiveExpression(t_l,'rule',0),' ',linksymbol,' ',recursiveExpression(t_r,'rule',1)];

end