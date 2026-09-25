class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        s = expression
        n = len(s)
        i = 0

        def product(A, B):
            return {a + b for a in A for b in B}

        def parse_expr():
            nonlocal i

            result = parse_term()

            while i < n and s[i] == ',':
                i += 1
                result |= parse_term()

            return result

        def parse_term():
            nonlocal i

            result = {""}

            while i < n and s[i] not in '},':
                if s[i] == '{':
                    i += 1
                    part = parse_expr()
                    i += 1   # skip '}'
                else:
                    part = {s[i]}
                    i += 1

                result = product(result, part)

            return result

        return sorted(parse_expr())