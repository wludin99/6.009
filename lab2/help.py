def maxProfit(prices):
        # memo = dict()
        # days = len(prices)
        # def helper(day=0,buy=True,transaction=1):
        #     if transaction == 5:
        #         return 0
        #     if day >= days:
        #         return 0
        #     try:
        #         return memo[(day,buy,transaction)]
        #     except:
        #         pass
        #     w = helper(day+1,not buy,transaction+1)+((-1)**buy)*prices[day]
        #     wo = helper(day+1,buy,transaction)
        #     memo[(day,buy,transaction)] = max(w, wo)
        #     return max(w,wo)
        # return helper()
        prices = prices[::-1]
        #get rid of duplicates
        old = prices.pop()
        single = [old]
        while prices:
            new = prices.pop()
            if old != new:
                single.append(new)
            old = new
        prices = single[::-1]
        turns = []
        first = prices.pop()
        ## make list of turning points
        turns.append(first)
        second = prices.pop()
        while prices:
            third = prices.pop()
            if (first-second)*(second-third) <= 0:
                if first != second or second != third:
                    turns.append(second)
            first = second
            second = third
        if turns[0] > turns[1]:
            turns = turns[1:]
        if third > turns[-1]:
            turns.append(third)

        #turns -> pairs
        pairs = []
        for i in range(int(len(turns)/2)):
            pairs.append((turns[2*i],turns[2*i+1]))




        return pairs


prices = [2,1,1,2,3,1,0,1,4,5,4,5,5,5]
print(maxProfit(prices))


d = {1:2,3:1}
print(max(d,key=lambda x:d[x]))
