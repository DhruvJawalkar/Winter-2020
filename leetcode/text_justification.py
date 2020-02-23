class Solution:

def get_space_justified_text(self, group, maxWidth, isLast):
    if(len(group)==1):
        justified_text = group[0].ljust(maxWidth)
        return justified_text
    elif(isLast):
        justified_text = ' '.join([w for w in group])
        return justified_text.ljust(maxWidth)
    else:
        #calculate total space to distribute
        #cycle idx from 1 -> (len(group)-1)
        #prepend ' ' to each word
        #do till space is distributed
        space = maxWidth - sum([len(w) for w in group])
        idx = 1
        while(space):
            group[idx] = group[idx].rjust(len(group[idx])+1)
            space-=1
            idx+=1
            if(idx==len(group)):
                idx=1
        justified_text = ''.join([w for w in group])
        return justified_text

def add_spaces_to_word_groups(self, word_groups, maxWidth):
    #add spaces in round robin fashion for each word group
    res = []
    
    for idx, group_arr in enumerate(word_groups):
        res.append(self.get_space_justified_text(group_arr, maxWidth, idx==len(word_groups)-1))
    return res


def get_word_groups(self, words, maxWidth):
    groups = []
    
    cur_group = []
    cur_group_length=0
    
    for item in words:
        if(cur_group==[]):
            cur_group.append(item)
            cur_group_length+=len(item)
        elif(cur_group_length+1+len(item)<=maxWidth):
            cur_group.append(item)
            cur_group_length+=len(item)+1
        else:
            groups.append(cur_group)
            cur_group = []
            cur_group.append(item)
            cur_group_length=len(item)
    groups.append(cur_group)
    return groups
    
    
def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    
    word_groups = self.get_word_groups(words, maxWidth)
    res = self.add_spaces_to_word_groups(word_groups, maxWidth)
    
    return res
    
