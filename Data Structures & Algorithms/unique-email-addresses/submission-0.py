class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        raw = []

        for i in emails:
            local , domain = i.split('@')
            local = local.replace('.','').split("+")[0]
            email = local + '@' + domain
            if email not in raw:
                raw.append(email)
        return len(raw)