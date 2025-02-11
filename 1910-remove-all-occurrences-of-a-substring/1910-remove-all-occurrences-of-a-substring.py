class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st=[]
        m=len(part)
        for ch in s:
            st.append(ch)
            if len(st)>=m:
                st_ch="".join(st[-m:])
                if st_ch==part:
                    for r in range(m):
                        st.pop()
        return "".join(st)