from datetime import datetime

class Solution:
    def is_valid_time(self, h_1, h_0, m_1, m_0):
        if(((h_1<=2 and h_0<=3) or (h_1<=1 and h_0<=9)) and m_1<=5):
            return True
        return False
    
    def nextClosestTime(self, time: str) -> str:
        hh_mm = time.split(":")
        nums = []
        nums.append(int(hh_mm[0][0]))
        nums.append(int(hh_mm[0][1]))
        nums.append(int(hh_mm[1][0]))
        nums.append(int(hh_mm[1][1]))
        
        all_possible_times = []
        
        for h_1 in nums:
            for h_0 in nums:
                for m_1 in nums:
                    for m_0 in nums:
                        if(self.is_valid_time(h_1, h_0, m_1, m_0)):
                            new_time_str = str(h_1)+str(h_0)+":"+str(m_1)+str(m_0)
                            if(new_time_str != time):
                                all_possible_times.append(new_time_str)
       
        t_deltas = []
        FMT = '%H:%M'
        
        for possible_time in all_possible_times:
            tdelta = datetime.strptime(possible_time, FMT) - datetime.strptime(time, FMT)
            t_deltas.append(tdelta.seconds)
        
        if(len(t_deltas)):
            least_time_idx = t_deltas.index(min(t_deltas))
            return all_possible_times[least_time_idx]
        else:
            return time
        
        
