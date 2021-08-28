class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        start = total = sub_total = 0
        for index in range(len(gas)):
            net_gas = gas[index] - cost[index]
            total += net_gas
            sub_total += net_gas
            if sub_total < 0:
                sub_total = 0
                start = index + 1
        return start if total >= 0 else -1

#        start = None
#        total = sub_total = 0
#        for index, (gas_add, gas_cost) in enumerate(zip(gas, cost)):
#            net_gas = gas_add - gas_cost
#            total += net_gas
#            if start is not None:
#                sub_total += net_gas
#                if sub_total < 0:
#                    start = None
#                    sub_total = 0
#            elif start is None and net_gas >= 0:
#                start = index
#                sub_total = net_gas
#        return start if total >= 0 else -1


if __name__ == '__main__':
    gas = [2,3,4]
    cost = [3,4,3]
    print(Solution().canCompleteCircuit(gas, cost))

