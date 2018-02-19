
# Implement a Job Scheduler with these two methods:
# # addJob(J job, priority, Set<J> dependencies)
# # runAllJobs()
#
# - Try to run job with highest priority first, but:


# 'foo' : ['bar', 'baz']
# 'bar' : ['boo']
# 'baz' : []
# 'boo' : []


#     addJob('foo', 10, ['bar','baz'])
#     addJob('bar', 5, ['boo'])
#     addJob('baz', 1, [])
#     addJob('boo', 4, [])

#     runAllJobs()

#     - boo, bar, baz, foo

from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.dependency_dict = defaultdict(list)
        self.jobList = []

    def addJob(self, job, priority, dependency_set):
        self.jobList.append((job, priority))
        self.jobList.sort(key=lambda x: x[1])

        if job not in self.dependency_dict:
            self.dependency_dict[job] = dependency_set

    def displaydependencydict(self):
        print self.dependency_dict

    def runAllJobs(self):
        i = len(self.jobList) -1
        while i >= 0:
            job, priority = self.jobList[i]
            dep = set()
            self.getdependencyRecursive(job, dep)
            dep.add(job)
            for x in list(dep):
                if x in self.dependency_dict:
                    del self.dependency_dict[x]
                j = 0
                while j < len(self.jobList):
                    job, priority = self.jobList[j]
                    if job == x:
                        self.jobList.pop(j)
                    j += 1
            i = len(self.jobList) - 1
            i -= 1
            print list(dep)[::-1]

    def getdependencyRecursive(self, job, dep):
        if job not in self.dependency_dict:
            return
        elif job in self.dependency_dict:
            for v in self.dependency_dict[job]:
                self.getdependencyRecursive(v, dep)
                dep.add(v)


S = Solution()
S.addJob('foo', 10, ['bar' ,'baz'])
S.addJob('bar', 5, ['boo'])
S.addJob('baz', 1, [])
S.addJob('boo', 4, [])
# S.displaydependencydict()
S.runAllJobs()