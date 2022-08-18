#Valid Parentheses - Grind75 & TIQ

s = "(]"

#Approach : Stack
#TC : O(n), SC: O(n)
def func(s):
    st = []
    for i in s:
        if(i not in (")","]","}")): st.append(i)
        else:
            if(not len(st)): return False
            t = st.pop()
            if((t == "(" and i != ")") or (t == "[" and i != "]") or (t == "{" and i != "}")): return False
    if(len(st)): return False
    return True

print(func(s))