class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            # "m.y+name@email.com" will be forwarded to "my@email.com".
            local = local.split("+")[0]
            # "alice.z@neetcode.io" and "alicez@neetcode.io" forward to the same email address.
            local = local.replace(".", "")
            unique.add((local, domain))
        return len(unique)