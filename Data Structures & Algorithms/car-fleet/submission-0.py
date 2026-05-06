class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # input: 2 arrays (same length) (position and speed of the ith car)
        #        1 integer (target distance)
        # of car fleets is the number of cars that arrive at the same time t
        
        stack, cars = [], len(position)

        pairs = sorted(zip(position,speed), reverse = True)
        time = [0] * cars


        for i in range(cars):
                time[i] = (target - pairs[i][0]) / pairs[i][1]
                if not stack or time[i] > stack[-1]:
                        stack.append(time[i])
        return len(stack)