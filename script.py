import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
utm_source_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(utm_source_count)
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.notnull()
print(ad_clicks)
click_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
clicks_pivot = click_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
)
clicks_pivot['percent_clicked'] = clicks_pivot[True] /len(clicks_pivot)
print(clicks_pivot)
a_clicks = ad_clicks[(ad_clicks.experimental_group == 'A') & (ad_clicks.is_click == True)]
print(a_clicks.info())
b_clicks = ad_clicks[(ad_clicks.experimental_group == 'B') & (ad_clicks.is_click == True)]
print(b_clicks.info())

a_clicks_by_day = a_clicks.groupby('day').user_id.count().reset_index()
b_clicks_by_day = b_clicks.groupby('day').user_id.count().reset_index()

a_clicks_by_day['percent_clicked_a'] = a_clicks_by_day['user_id'] *100 / len(a_clicks)
print(a_clicks_by_day)

b_clicks_by_day['percent_clicked_b'] = b_clicks_by_day['user_id'] *100 / len(b_clicks)
print(b_clicks_by_day)

comparison = pd.merge(a_clicks_by_day, b_clicks_by_day)
print(comparison)


















