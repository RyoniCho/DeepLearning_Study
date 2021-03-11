from pandas import Series,DataFrame #Pandas 라이브러리 (dataframe,series)
import pandas_datareader.data as web #Pandas Data reader 라이브러리 
import datetime
import matplotlib.pyplot as plt



iamSeries=Series([100,200,150,200,300])
print(iamSeries)
'''
0    100
1    200
2    150
3    200
4    300
dtype: int64

Pandas Series :
인덱스는 0부터시작. 인덱스값과 밸류값을 같이 저장하고있음. 1차원 배열과비슷하다.
'''


iamSeries2=Series([100,200,150,200,300],index=['2020-12-01','2020-12-02','2020-12-03','2020-12-04','2020-12-05'])

print(iamSeries2)

'''

2020-12-01    100
2020-12-02    200
2020-12-03    150
2020-12-04    200
2020-12-05    300
dtype: int64

인덱스 값을 이런식으로 지정해줄수있다. 1차원배열+딕셔너리의 자료구조스타일이라고 할수있다. 
'''

print(iamSeries2['2020-12-05']) #300
'''
요렇게 키값으로 접근이 가능하다. 

'''

iamSeries3=Series([1,2,3],index=['a','a','b'])

print(iamSeries3)

'''

a    1
a    2
b    3
dtype: int64

인덱스 지정했을때 딕셔너리랑 비슷하다는것이지 같다는건 아니다. index를 동일한값으로 넣어줘도 키충돌에러같은건 발생하지않는다.
순서대로 그냥 무식하게 들어간다. 
'''

print(iamSeries3['a'])

'''
a    1
a    2
dtype: int64

그래서 요렇게 동일 인덱스 접근시 두개가 나온다. 같은 인덱스를 가지고있는게 2개있으니까 다 토해낸다.
'''

for s in iamSeries2.index:
    print(s)

print('='*20)
for s in iamSeries2.values:
    print(s)

'''

2020-12-01
2020-12-02
2020-12-03
2020-12-04
2020-12-05
====================
100
200
150
200
300

index, values로 각각 접근가능하다.
'''


#series객체의 인덱스 순서가 다르더라도 매칭해서 더해줄수도있다.
iamSeries4=Series([10,20,30],index=['kor','eng','jpn'])
iamSeries5=Series([5,40,100],index=['jpn','eng','kor'])

mergeSeries=iamSeries4+iamSeries5

print(mergeSeries)

'''
eng     60
jpn     35
kor    110
dtype: int64

'''

dicStatus={"lv":[1,2,3],"hp":[100,150,200],"mp":[200,250,300]}

dfStatus=DataFrame(dicStatus)

print(dfStatus)

'''
   lv   hp   mp
0   1  100  200
1   2  150  250
2   3  200  300

'''

print(dfStatus['hp'])
print(type(dfStatus['hp']))


'''
0    100
1    150
2    200
Name: hp, dtype: int64
<class 'pandas.core.series.Series'>

'''

dfStatus2=DataFrame(dicStatus,index=["LV1","LV2","LV3"])
print(dfStatus2)

'''
     lv   hp   mp
LV1   1  100  200
LV2   2  150  250
LV3   3  200  300

DataFrame도 인덱스 바꾸는것이 가능하다.
'''


#print(dfStatus[0]) #KEY ERROR
#print(dfStatus2['LV1']) #KEY ERROR

'''
dataframe에서 []은 column의 키값으로만 인식.
이때에는 키에러가 발생한다. 

row접근을 위해서는 loc키워드 필요
'''

print(dfStatus2.loc['LV1'])
print(type(dfStatus2.loc['LV1']))

'''
lv      1
hp    100
mp    200
Name: LV1, dtype: int64

<class 'pandas.core.series.Series'>

loc로 row접근이 가능하다.
이렇게 접근된 객체도 시리즈로 이루어져있다. 

'''



start=datetime.datetime(2020,1,1)
end=datetime.datetime(2020,12,20)

samsung=web.DataReader("005935","naver",start,end)
# plt.plot(samsung['Close'])
# plt.show()

# print(samsung.tail())
# print(samsung.info())

ma5=samsung['Close'].rolling(window=5).mean()

#print(ma5.tail(10))

samsung.insert(len(samsung.columns),"MA5",ma5)
print(samsung.tail(10))


print(dfStatus2)


for index in range(len(dfStatus2)):
    print(dfStatus2.iloc[index])









    
    