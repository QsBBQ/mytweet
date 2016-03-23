import json
import pandas as panda
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import re

tweets_data_path = 'tweet_mining.json'

def read_json(file_path):
    results = []
    tweets_file = open(tweets_data_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

results  = read_json(tweets_data_path)
#create  a dataframe
statuses = panda.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
#store the languge values
statuses['lang'] = map(lambda status: status['lang'], results)
#sometines there may not be a 'place' listed in the tweet , so set to 'None' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

#  new DataFrame columns
statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))
statuses['java']   = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))
statuses['c#']     = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))
statuses['ruby']   = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))

# output the number of tweets where it is True that they contain our keywords
# output the number of tweets where it is True that they contain our keywords
print statuses['python'].value_counts()[True]
print statuses['java'].value_counts()[True]
print statuses['c#'].value_counts()  #note this had no True
print statuses['ruby'].value_counts()[True]

slices = [statuses['python'].value_counts()[True],
          statuses['java'].value_counts()[True],
          statuses['ruby'].value_counts()[True]]

activities = ['python','java','ruby']
cols = ['c','m','r']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0.1,0,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()

#get each tweet language and the  count of its appearance (not to be confused with programming languages)
# tweets_by_lang = statuses['lang'].value_counts()
# print(tweets_by_lang)
# # create our drawing space/window (figure)
# fig = plt.figure()
# # add a plot area for our data on the figure - 1,1,1 means a single chart/graph
# ax = fig.add_subplot(1,1,1)
#
# #style the axes and labels of our plot
# ax.tick_params(axis='x', labelsize=15)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Tweet Languages', fontsize=15)
# ax.set_ylabel('Number of tweets' , fontsize=15)
# ax.xaxis.label.set_color('#666666')
# ax.yaxis.label.set_color('#666666')
# ax.tick_params(axis='x', colors='#666666')
# ax.tick_params(axis='y', colors='#666666')
# #style the title
# ax.set_title('Top 10 languages', fontsize=15, color='#666666')
#
# #plot the top 10 tweet languages and appearance count using a bar chart
# tweets_by_lang[:10].plot(ax=ax, kind='bar', color='#FF7A00')
#
# #color the spines (borders)
# for spine in ax.spines.values():
#         spine.set_edgecolor('#666666')
#
# # render the graph
# plt.show()

#get each tweet language and the  count of its appearance (not to be confused with programming languages)
# tweets_by_lang = statuses['lang'].value_counts()
# # get each tweet country of origin and the count of its appearance
# tweets_by_country = statuses['country'].value_counts()
#
# # create our drawing space (figure)
# fig = plt.figure()
#
#
# # prepare to plot two charts on the same figure
# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)
#
# #style the axes
# ax1.tick_params(axis='x', labelsize=15)
# ax1.tick_params(axis='y', labelsize=10)
# ax1.set_xlabel('Tweet Languages', fontsize=15)
# ax1.set_ylabel('Number of tweets' , fontsize=15)
# ax1.xaxis.label.set_color('#666666')
# ax1.yaxis.label.set_color('#666666')
# ax1.tick_params(axis='x', colors='#666666')
# ax1.tick_params(axis='y', colors='#666666')
# #style the title
# ax1.set_title('Top 10 languages', fontsize=15, color='#666666')
#
# #plot the top 10 tweet languages and appearance count using a bar chart
# tweets_by_lang[:10].plot(ax=ax1, kind='bar', color='#FF7A00')
#
# #color the spines (borders)
# for spine in ax1.spines.values():
#         spine.set_edgecolor('#666666')
#
# #Second subplot
# ax2.tick_params(axis='x', labelsize=15)
# ax2.tick_params(axis='y', labelsize=10)
# ax2.set_xlabel('Countries', fontsize=15)
# ax2.set_ylabel('Number of tweets' , fontsize=15)
# ax2.xaxis.label.set_color('#666666')
# ax2.yaxis.label.set_color('#666666')
# ax2.tick_params(axis='x', colors='#666666')
# ax2.tick_params(axis='y', colors='#666666')
# #style the title
# ax2.set_title('Top 10 Countries', fontsize=15, color='#666666')
#
# #plot the top 10 tweet languages and appearance count using a bar chart
# tweets_by_country[:10].plot(ax=ax2, kind='bar', color='#FF7A00')
#
# #color the spines (borders)
# for spine in ax2.spines.values():
#         spine.set_edgecolor('#666666')
#
# # render the two graphs at once
# plt.show()
