import pandas as pd

#getting dataframe from csv
df = pd.read_csv('test-task_dataset_summer_products.csv', usecols=['origin_country','rating_five_count', 'rating_count', 'price'], index_col=False)
pd.set_option("display.max_rows", None, "display.max_columns", None)

#sorting dataframe
df = df.sort_values(by=['origin_country'])

#getting avg(price)
df_grouped_avg = df.groupby('origin_country')['price'].mean()
avg_price = df_grouped_avg.tolist()
og_country = df_grouped_avg.index.tolist()

#getting sum(rating_five_count) and sum (rating_count)
sum_five = df.groupby('origin_country')['rating_five_count'].sum().tolist()
sum_count = df.groupby('origin_country')['rating_count'].sum().tolist()
five_percent = []

#calulating five_percentage (sum(rating_five_count)\sum(rating_count)*100
for i in range(0,len(sum_five)):
    if sum_count[i] != 0:
        result = (sum_five[i]/sum_count[i])*100
    else:
        result = 0 
    five_percent.append(result)

#forming new frame with origin_country, avg(price), and five percentage
frame = {'origin_country': og_country,'avg_price': avg_price, 'five_percent': five_percent}
new_frame = pd.DataFrame(frame)

#print new frame
print(new_frame)

#creating output.csv for futher analyzis
new_frame.to_csv('output.csv', index=False)
print("Output.csv is created.")



