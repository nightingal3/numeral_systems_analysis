function [t] = constructTree(elements,opt)

if strmatch('ONE',opt,'exact')
    
    t = tree(elements);
    
elseif strmatch('GAU',opt,'exact')
    
    t = tree('GAU');
    [t,n_l] = t.addnode(1,elements);
    
elseif strmatch('SUC',opt,'exact')
    
    t = tree('SUC');
    
    ele = '';
    if iscell(elements)
        for i = 1:length(elements)
            ele = [ele,' ',elements{i}];
        end
    else
        ele = elements;
    end
    %[t,n_l] = t.addnode(1,'MEA');
    %[t,n_l_l] = t.addnode(n_l,ele);

    [t,n_l] = t.addnode(1,ele);
   
    
    %{
    if iscell(elements) && length(elements) > 1
    for i = 1:length(elements)
            [t,nn] = t.addnode(1,elements{i});
        end
    else
        %ele = elements;
        [t,n_l] = t.addnode(1,elements);
    end
    %}
    
    
    
elseif strmatch('HIG',opt,'exact')
    
    %t = tree('HIG');
    %[t,n_l] = t.addnode(1,elements);
    t = tree('HIG');
    %[t,n_l] = t.addnode(1,'MEA');
    %[t,n_l_l] = t.addnode(n_l,elements);
 
    [t,n_l] = t.addnode(1,elements);
 
elseif strmatch('ADD',opt,'exact')
    
    t = tree('ADD');
    [t,n_l] = t.addnode(1,'MEA');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,elements{1});
    [t,n_r_l] = t.addnode(n_r,elements{2});
    
elseif strmatch('SUB',opt,'exact')
    
    t = tree('SUB');
    [t,n_l] = t.addnode(1,'MEA');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,elements{1});
    [t,n_r_l] = t.addnode(n_r,elements{2});
    
elseif strmatch('MUL',opt,'exact')
    
    t = tree('MUL');
    [t,n_l] = t.addnode(1,'MEA');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,elements{1});
    [t,n_r_l] = t.addnode(n_r,elements{2});

elseif strmatch('DIV',opt,'exact')
    
    t = tree('DIV');
    [t,n_l] = t.addnode(1,'MEA');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,elements{1});
    [t,n_r_l] = t.addnode(n_r,elements{2});
        
elseif strmatch('MULADD',opt,'exact')
    
    t = tree('ADD');
    [t,n_l] = t.addnode(1,'MUL');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,'MEA');
    [t,n_l_r] = t.addnode(n_l,'MEA');
    [t,n_l_l_l] = t.addnode(n_l_l,elements{1});
    [t,n_l_r_l] = t.addnode(n_l_r,elements{2});
    [t,n_r_l] = t.addnode(n_r,elements{3});

    
elseif strmatch('MULSUB',opt,'exact')
    
    t = tree('SUB');
    [t,n_l] = t.addnode(1,'MUL');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,'MEA');
    [t,n_l_r] = t.addnode(n_l,'MEA');
    [t,n_l_l_l] = t.addnode(n_l_l,elements{1});
    [t,n_l_r_l] = t.addnode(n_l_r,elements{2});
    [t,n_r_l] = t.addnode(n_r,elements{3});
    
elseif strmatch('MULADDADD',opt,'exact')
    
    t = tree('ADD');
    [t,n_l] = t.addnode(1,'ADD');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,'MUL');
    [t,n_l_l_l] = t.addnode(n_l_l,'MEA');
    [t,n_l_l_r] = t.addnode(n_l_l,'MEA');
    [t,n_l_l_l_l] = t.addnode(n_l_l_l,elements{1});
    [t,n_l_l_r_l] = t.addnode(n_l_l_r,elements{2});
    [t,n_l_r] = t.addnode(n_l,'MEA');
    [t,n_l_r_l] = t.addnode(n_l_r,elements{3});
    [t,n_r_l] = t.addnode(n_r,elements{4});

elseif strmatch('ADDADD',opt,'exact')
    
    t = tree('ADD');
    [t,n_l] = t.addnode(1,'ADD');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,'MEA');
    [t,n_l_r] = t.addnode(n_l,'MEA');
    [t,n_l_l_l] = t.addnode(n_l_l,elements{1});
    [t,n_l_r_l] = t.addnode(n_l_r,elements{2});
    [t,n_r_l] = t.addnode(n_r,elements{3});
    
elseif strmatch('POW',opt,'exact')
    
    t = tree('POW');
    [t,n_l] = t.addnode(1,'MEA');
    [t,n_r] = t.addnode(1,'MEA');
    [t,n_l_l] = t.addnode(n_l,elements{1});
    [t,n_r_l] = t.addnode(n_r,elements{2});
    
elseif strmatch('MEM',opt,'exact')
    
    t = tree('');
    for i = 1:length(elements)
        [t,nn] = t.addnode(1,elements{i});
    end
    
elseif strmatch('EQU',opt,'exact')
    
    t = tree(elements);
    
elseif strmatch('FORM',opt,'exact')
    
    if iscell(elements)
        t = tree('');
        for i = 1:length(elements)
            [t,nn] = t.addnode(1,elements{i});
        end
    else
        t = tree(elements);
    end
    
else
    
    disp('Error: command does not exist!')
    
end


end