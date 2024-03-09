class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        anchor = len(logs) - 1
        for i in range(len(logs)-1, -1, -1):
            space = logs[i].index(' ')
            if logs[i][space+1].isdigit():
                logs[i], logs[anchor] = logs[anchor], logs[i]
                anchor -= 1
            else:
                logs[i] = logs[i][space+1:], logs[i][:space]
                
        logs[:anchor+1] = sorted(logs[:anchor+1])
        for i in range(anchor+1):
            logs[i] = logs[i][1] + ' ' + logs[i][0]
        return logs
