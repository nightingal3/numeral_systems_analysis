function [commd,rule,num,numnodes,depths,t_l,t_r] = SUC(forms,numexp)

num = numexp;

for i = 2:length(forms)
    
    j = i - 1;
    
    % Construct left (forms) and right (rule) trees
    [t_l{j}] = constructTree(forms{i},'FORM');
    [t_r{j}] = constructTree(forms{j},'SUC');
    
    % Concatonate left and right trees
    [commd{j} rule{j}] = linkLeftRightExpressions(t_l{j},t_r{j},'=');
    
    % Calculate complexity
    %numnodes{j} = nnodes(t_l{j}) + nnodes(t_r{j}) + 1 - (nnodes(t_r{j})>2);
    numnodes{j} = nnodes(t_l{j})  - (depth(t_l{j})>0) + nnodes(t_r{j}) + 1;
    depths{j} = [depth(t_l{j}) depth(t_r{j})];
    
    
end

