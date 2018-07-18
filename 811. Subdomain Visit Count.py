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
            sub = list(reversed(val[1].split('.')))
            curr = ''
            for dom in sub:
                if len(curr):
                    curr = dom + '.' + curr
                else:
                    curr = dom
                if curr in domain:
                    domain[curr] += int(count)
                else:
                    domain[curr] = int(count)
        for key,val in domain.items():
            ans.append(str(val)+' '+key)
        return ans
inp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(Solution().subdomainVisits(inp))