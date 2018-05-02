function [ind rule] = linkRuleToCommand(commd)

commdandset = {'ONE','GAU','MEA','SUC','HIG','ADD','SUB','MUL','DIV','POW','DEF','MEM','EQU'};

ind = strmatch(commd,commdandset,'exact');

if ~isempty(ind)
    
    ruleset = {'r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13'};
    
    rule = ruleset{ind};
    
else
    
    ind = 0;
    rule = 0;
    
end

end