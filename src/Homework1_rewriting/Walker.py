import random

class Walker:
    def __init__(self, events):
        #events - список пар: [(событие1, вероятность1), (событие2, вероятность2), ...]
        
        if not events:
            raise ValueError("Список событий не может быть пустым!")
        
        for event, prob in events:
            if prob < 0:
                raise ValueError(f"Вероятность для события '{event}' отрицательная: {prob}")
        
        total = sum(prob for _, prob in events)
        if abs(total - 1.0) > 0.0001:
            raise ValueError(f"Сумма вероятностей должна быть 1, а получилось {total}")
        
        self.events = events
        n = len(events)
        
        self.q = [0.0] * n  
        self.y = [0] * n    
        self.events_list = [event for event, _ in events]  
        
        for i in range(n):
            self.q[i] = n * events[i][1]
        
        small = []
        large = []
        
        for i in range(n):
            if self.q[i] < 1.0:
                small.append(i)
            else:
                large.append(i)
        
        while small and large:
            s = small.pop()
            l = large.pop()
            
            self.y[s] = l
            

            self.q[l] = self.q[l] - (1.0 - self.q[s])
            

            if self.q[l] < 1.0:
                small.append(l)
            else:
                large.append(l)

        for i in small + large:
            self.y[i] = i
            self.q[i] = 1.0
    
    def get_random(self):
        n = len(self.events)
        
        i = random.randint(0, n-1)
        
        u = random.random()
        
        if u < self.q[i]:
            return self.events_list[i]
        else:
            return self.events_list[self.y[i]]


