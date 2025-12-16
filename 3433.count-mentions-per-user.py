#
# @lc app=leetcode id=3433 lang=python3
#
# [3433] Count Mentions Per User
#

# @lc code=start
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        offline_users = dict()

        events = [[0 if e[0] == "OFFLINE" else 1, int(e[1]), e[2]] for e in events]
        events.sort(key=lambda x: (x[1], x[0]))

        for event in events:
            if event[0] == 0:
                time_stamp, user_id = event[1], int(event[2])
                offline_users[user_id] = time_stamp + 60
            else:
                time_stamp, message = event[1], event[2]
                if message == "ALL":
                    mentions = [mentions[i] + 1 for i in range(numberOfUsers)]
                elif message == "HERE":
                    tmp_users = set()
                    for user_id, offline_time in offline_users.items():
                        if offline_time <= time_stamp:
                            tmp_users.add(user_id)

                    for user_id in tmp_users:
                        offline_users.pop(user_id)
                    
                    for user_id in range(numberOfUsers):
                        if user_id not in offline_users:
                            mentions[user_id] += 1
                else:
                    mention_users = message.split(' ')
                    mention_users = [int(uid[2:]) for uid in mention_users]
                    for user_id in mention_users:
                        mentions[user_id] += 1
        return mentions
                    

    
        
# @lc code=end

