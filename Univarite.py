class Univarite():
    
    def init(self):
        pass
    
    def QuanQual(self,dataset):
        Quan=[]
        Qual=[]
        for column in dataset.columns:
            #print(column)
            if(dataset[column].dtypes=='object'):
                Qual.append(column)
            else:
                Quan.append(column)
        print("Quan:",Quan)
        print("Qual:",Qual)
        return Quan,Qual

    def freqTable(self,columnName,dataset):
        import pandas as pd
        frq=pd.DataFrame()
        frq["Unique_Values"]=dataset[columnName].value_counts().index
        frq["Frequency"]=dataset[columnName].value_counts().values
        frq["Relative_Fre"]=dataset[columnName].value_counts().values/len(dataset[columnName])*100
        frq["Cumulative"]=frq["Relative_Fre"].cumsum()
        return frq