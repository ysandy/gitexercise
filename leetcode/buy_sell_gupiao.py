#买：第n个数比第n+1个数小：买，n从0开始
#卖：第n个数比第n-1个数大：卖，n从1开始
# [1,2,3,4,5]   [7,6,4,3,1]  [1,2,1,4,5] [7,1,5,3,6,4] [1,2,3,2,5,6,3]
prices=[1,2,3,2,5,6,3]
#0-5
buy = 0
sell = 0
b = 0
for i in range(len(prices)-1):
    #买的情形：b=0,[s=0，s=1];
    # 卖的情形：b=1,s=0
    #没买过股票，或者卖出了
    if b==0 and prices[i]<prices[i+1]: #买入点
        buy += prices[i]
        b = 1
    if b==1 :
        if prices[i-1]<prices[i] and prices[i]>prices[i+1]:  #卖出点
            sell += prices[i]
            b = 0
        else:
            sell += prices[i+1]
            b = 0
ly = sell-buy
print(ly)

# 关于这题：因为最优解只有一个，既然是最优，那么就往最好的地方去想，今天买的和明天买的差值如果有赚我就今天买明天卖了，
# 不然我就不买不卖。有人会问，那我今天买的明天卖了，万一后天股票价格比我明天卖的更贵那我不是卖早了亏了吗，
# 确实是这样，但是因为是程序，我们有数据我们就可以预知未来，只是一个模拟罢了，并且，因为现实中对股票价格的不可预测性，
# 我们不可能真的乱买乱卖。但是程序有数据能预测我们只是做一个模拟的话是可以求出最优解的。比如2 4 9，来说，我应该今天买后天卖，最优解为
# 9 - 2 = 7；那我就不能明天卖，应该后天卖，但是程序它不知道啊，我们这样想，
# 明天卖早了说明我明天买后天在卖还是有钱赚，并且和后天卖的钱挣得是一样的即：4 - 2 + 9 - 4 = 7；
# 当然现实中我们不可以这样买卖，只是求最优解的话是可以的。
#
# class Solution {
# public int maxProfit(int[] prices) {
# int ans = 0;
#
# // 记录差值
# int Dvalue = 0;
# for (int i = 0; i < prices.length - 1; i++){
#     Dvalue = prices[i+1] - prices[i];
#     if (Dvalue > 0){
#         ans += Dvalue;
# }
# }
#
#
# return ans;
# }
# }

# 由于可以在同一天卖出和买入，这相当于没有卖出，连续买。因此只要比对当前与前一天的价格（即这两天能获得的利润），
# 如果是上升的就加上，如果是下降的则取0，最后所有的连续日利润的和就是最大利润。
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(len(prices)-1):
#             max_profit += max(0, prices[i+1]-prices[i])
#         return max_profit

