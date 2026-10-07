class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = {}

        for day in responses:
            for word in set(day):
                count[word] = count.get(word, 0) + 1

        max_count = max(count.values())

        # Return lexicographically smallest word if tied
        answer = ""
        for word in count:
            if count[word] == max_count:
                if answer == "" or word < answer:
                    answer = word

        return answer