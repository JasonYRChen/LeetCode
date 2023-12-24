class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        for cp in cpdomains:
            count, domain = cp.split()
            count = int(count)
            while domain:
                counter[domain] += count
                next_dot = domain.find('.')
                next_dot = next_dot if next_dot > 0 else len(domain)
                domain = domain[next_dot + 1:]
        return [f'{v} {k}' for k, v in counter.items()]
