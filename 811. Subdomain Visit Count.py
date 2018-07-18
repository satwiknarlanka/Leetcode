class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain = {}
        ans = []
        for inp in cpdomains:
            val = inp.split()
            count = val[0]
            sub = reversed(val[1].split('.'))
            curr = ''
            for dom in sub:
                curr = dom + '.' + curr if len(curr) else dom
                domain[curr] = domain[curr] + int(count) if curr in domain else int(count)
        for key,val in domain.items():
            ans.append(str(val)+' '+key)
        return ans
inp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(Solution().subdomainVisits(inp))