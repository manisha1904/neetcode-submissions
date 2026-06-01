class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        length = len(position)
        cars = sorted(zip(position, speed), reverse=True)

        for pos, v in cars:
            t = (target - pos) / v
            stack.append(t)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
