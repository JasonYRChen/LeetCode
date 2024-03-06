class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        answer = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            new_email = local + '@' + domain
            answer.add(new_email)
        return len(answer)
