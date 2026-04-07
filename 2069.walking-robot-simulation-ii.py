#
# @lc app=leetcode id=2069 lang=python3
#
# [2069] Walking Robot Simulation II
#

# @lc code=start
class Robot:

    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self.pos = [0, 0]
        self.dir = "East"
        self.transition_map = {
            "East": "North", 
            "North": "West", 
            "West": "South", 
            "South": "East"
        }
        self.perimeter = (width - 1 + height - 1) * 2 

    def step(self, num: int) -> None:
        while(num):
            if self.dir == "North":
                if self.pos[1] == self.height - 1:
                    self.dir = self.transition_map[self.dir]
                    continue
                new_pos = [self.pos[0], min(self.pos[1] + num, self.height - 1)]
                steps = new_pos[1] - self.pos[1]
                num -= steps 
                self.pos = new_pos
                if self.pos[1] == self.height - 1:
                    num %= self.perimeter
            elif self.dir == "South":
                if self.pos[1] == 0:
                    self.dir = self.transition_map[self.dir]
                    continue
                new_pos = [self.pos[0], max(self.pos[1] - num, 0)]
                steps = self.pos[1] - new_pos[1]
                num -= steps
                self.pos = new_pos
                if self.pos[1] == 0:
                    num %= self.perimeter
            elif self.dir == "West":
                if self.pos[0] == 0:
                    self.dir = self.transition_map[self.dir]
                    continue
                new_pos = [max(self.pos[0] - num, 0), self.pos[1]]
                steps = self.pos[0] - new_pos[0]
                num -= steps 
                self.pos = new_pos
                if self.pos[0] == 0:
                    num %= self.perimeter
            else: 
                if self.pos[0] == self.width - 1:
                    self.dir = self.transition_map[self.dir]
                    continue
                new_pos = [min(self.pos[0] + num, self.width - 1), self.pos[1]]
                steps = new_pos[0] - self.pos[0]
                num -= steps 
                self.pos = new_pos   
                if self.pos[0] == self.width - 1:
                    num %= self.perimeter

    def getPos(self) -> List[int]:
        return self.pos         

    def getDir(self) -> str:
        return self.dir        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# @lc code=end

