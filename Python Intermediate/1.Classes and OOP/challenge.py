class Student:

    scores = [65,75,85,95]
    count = 0

    def average_score(self):    
        for score in self.scores:
            self.count += 1
        return sum(self.scores) / self.count

print(int(Student().average_score()))
  



