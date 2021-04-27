class Solution:

    def taketasks(self, tasks, num):
        # Takes away num different tasks
        # print( "Taking away {} tasks".format(num))
        for i in range(0, len(tasks) ):
            if num <= 0:
                tasks.sort(reverse=True)
                return tasks
            if tasks[i] > 0:
                tasks[i] -= 1
                num -= 1
        if num > 0: raise RuntimeError("Not enough tasks")
        else:
            tasks.sort(reverse=True)
            return tasks

    def leastInterv(self, tasks, n, idle):
        num_tasks = len( list( filter( lambda x: x > 0, tasks ) ) )
        # print( tasks )
        # print( num_tasks )
        # print( n + 1 )
        if num_tasks == 0: return 0
        elif (n+1) > num_tasks:
            return idle + num_tasks + self.leastInterv(list( map( lambda i: i-1, tasks)), n, (n+1)-num_tasks)
        else:
            tasks = self.taketasks(tasks, n+1)
            return idle + n + 1 + self.leastInterv(tasks, n, 0)
    
    def leastInterval(self, tasks, n):
        memo = {}
        index = 0
        tasks_list = []
        for task in tasks:
            if task not in memo:
                memo[task] = index
                index += 1
                tasks_list.append(1)
            else:
                tasks_list[ memo[task] ] += 1
        tasks_list.sort(reverse=True)
        return self.leastInterv( tasks_list, n, 0 )
