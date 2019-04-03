import pandas as pd
import numpy as np

df_user_balance_table = pd.read_csv('user_balance_table.csv')
df_user_balance_table['report_date'].nunique()
df_user_balance_table.head()

df=df_user_balance_table.groupby(['report_date'])['total_purchase_amt','total_redeem_amt'].sum()
df.head(3)
df.reset_index(inplace=True)

df['date']=pd.to_datetime(df['report_date'],format='%Y%m%d')

df['weekday']=df['date'].dt.dayofweek
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month

from sklearn.preprocessing import LabelBinarizer,LabelEncoder,OneHotEncoder

le=LabelEncoder()

df.loc[:,'weekday'::]=df.loc[:,'weekday'::].apply(le.fit_transform)

df.head(3)

interests=pd.read_csv('mfd_day_share_interest.csv')

df.shape
df1=pd.merge(df,interests,left_on='report_date',right_on='mfd_date',how='left')

shibor=pd.read_csv('mfd_bank_shibor.csv')

shibor.shape

df2=pd.merge(df1,shibor,left_on='report_date',right_on='mfd_date',how='left')
df2.shape

df2.isnull().sum()
df2.fillna(method='pad',inplace=True)


x=df2.loc[:,'weekday'::].drop(['mfd_date_x','mfd_date_y'],axis=1)
y=df2[['total_purchase_amt','total_redeem_amt']]

from sklearn.cross_validation import train_test_split

x1,x2,y1,y2=train_test_split(x,y,test_size=0.1,random_state=42)

y1_purchase=y1.total_purchase_amt
y1_redeem_amt=y1.total_redeem_amt

y2_purchase=y2.total_purchase_amt
y2_redeem_amt=y2.total_redeem_amt

import xgboost as xgb
xgtrain_pur=xgb.DMatrix(x1.values,y1_purchase.values)
xgtrain_redeem=xgb.DMatrix(x1.values,y1_redeem_amt.values)
xgtest=xgb.DMatrix(x2.values)


def evalerror(preds,xgtrain_pur):
    labels=xgtrain_pur.get_label()
    err=np.divide(np.abs(preds-labels),labels)
    return 'pur_error',np.sum(err)/len(labels)

 num_round=100

 params={'booster': 'gblinear',
        'objective':'reg:linear',
        'eval_metric':'rmse',
        'seed': 10
       }

 model=xgb.train(params,xgtrain_pur,num_round)
 preds_pur=model.predict(xgtest_pur)


from sklearn.metrics import mean_squared_error
mean_squared_error(preds_pur,y2_purchase)


from xgboost import plot_importance
plot_importance(model)