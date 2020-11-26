# https://leetcode.com/problems/unique-email-addresses/submissions/
class Solution(object):
    def numUniqueEmails(self, emails):

        newSet = set()

    
        for email in emails:

            local = email[:email.index("@")]
            domain = email[email.index("@"):]

            if "+" in local:
                local = local[:local.index("+")]

            local = local.replace(".", "")

            newSet.add(local + domain)
        return (len(newSet))


