function [expression] = recursiveExpression(t,opt,LorR)
% Recursively traverse tree and combine expressions
% Recursion top-down: combined expression = parent ( child_1 child_2 child_3 ... )
% LorR = 0 for left form expression; = 1 for right rule expression
% opt = 'rule' for rule-based expression; = 'command' for short command exp

if isempty(t.getchildren(1)) % No children
    
    % Leave nodes
    
    expression = t.Node{1};
    if strmatch(opt,'rule','exact')
        [ind rule] = linkRuleToCommand(expression);
        if ind ~= 0 && LorR == 1
            expression = rule; % Rule printout
        elseif ind == 0 && LorR == 1
            expression = 's';
        elseif ind == 0 && LorR == 0
            expression = 's'; % Form printout
        end
    end
    
else % With children
    
    % Non-leave nodes
    
    parentnode = t.Node{1};
    
    if strmatch(opt,'rule','exact')
        [ind rule] = linkRuleToCommand(parentnode);
        if ind ~= 0 parentnode = rule; end
    end
    
    childnodes = t.getchildren(1);
    
    if LorR == 1
        expression = [parentnode,' ( '];
    elseif LorR == 0
        if strmatch(opt,'rule','exact')
            if ~isempty(parentnode)
                expression = 's';
            else
                expression = '';
            end
        else
            expression = parentnode;
        end
    end
    
    for i = 1:length(childnodes) % Concatonate child nodes
        if LorR == 1
            if i < length(childnodes)
                expression = [expression, recursiveExpression(t.subtree(childnodes(i)),opt,LorR),' '];
            else
                expression = [expression, recursiveExpression(t.subtree(childnodes(i)),opt,LorR),' )'];
            end
        elseif LorR == 0
            expression = [expression, recursiveExpression(t.subtree(childnodes(i)),opt,LorR)];
        end
    end
    
end
