import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from DB_test import DB_test
import strategy

"""
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
"""

db=DB_test()
db.connectAndload()

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

"""             drawing            """  

"""
code of Plotly

fig = FF.create_candlestick(Open, high, low, close, date)

py.iplot(fig, filename='test', validate=False)
"""
ohlc = []
x = 0
y = len(db.date)

while x < y:
    append_me = mdates.date2num(db.date[x]), db.Open[x], db.high[x], db.low[x], db.close[x]
    ohlc.append(append_me)
    x+=1

candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#0066ff', colordown='#db3f3f')

for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

      
        
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))

ax1.grid(True)
plt.xlabel('Date')
plt.ylabel('Price')
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)



"""                                """

"""             srategy            """
#state[0] =0 means not holding , state[0] = 1 means holding;     
#state[1] = holding type;   state[1]  1 = buy ,   state[1] -1 =sell
#state[3] = price
state = [0,0,0]
goal = 0

for i in range(len(db.Open)):   
    behavior = strategy.policy(db.Open[i],db.high[i],db.low[i],db.close[i])

# if not holding
    if (state[0]==0):
        state[2] = db.close[i]
        if (behavior==1):
            ax1.annotate('buy', xy=(db.date[i], db.close[i]), xytext=(db.date[i], db.close[i]+80),
            arrowprops=dict(arrowstyle="->",facecolor='black'))
            state[1]=1
            state[0]=1
        elif(behavior==(-1)):
            ax1.annotate('sell', xy=(db.date[i], db.close[i]), xytext=(db.date[i], db.close[i]-80),
            arrowprops=dict(arrowstyle="->",facecolor='black'))
            state[1]=(-1)
            state[0]=1
#holding
    elif (state[0]==1):
        if(behavior== state[1]*(-1)):
            if(state[1]==-1):
                ax1.annotate('buy', xy=(db.date[i], db.close[i]), xytext=(db.date[i], db.close[i]+80),
                arrowprops=dict(arrowstyle="->",facecolor='black'))
                goal = goal + state[2] - db.close[i]
                state[2]=0
                state[0] = 0
            else:            
                goal = goal + db.close[i]- state[2]
                ax1.annotate('sell', xy=(db.date[i], db.close[i]), xytext=(db.date[i], db.close[i]-80),
                arrowprops=dict(arrowstyle="->",facecolor='black'))
                state[2]=0
                state[0] = 0
plt.show()
print (goal)
"""                                """
