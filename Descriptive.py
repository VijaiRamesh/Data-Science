import pandas as pd
class Descriptive():
    def init(self):
        pass
    def QuanQual(self,dataset):
        Quan=[]
        Qual=[]
        for column in dataset.columns:
            if(dataset[column].dtypes=='object'):
                Qual.append(column)
            else:
                Quan.append(column)
        print("Quan:",Quan)
        print("Qual:",Qual)
        return Quan,Qual
    
    def outliercolumn(self,quan,univariate):
        lesser=[]
        greater=[]
        for column in quan:
            if(univariate[column]["Min"]<univariate[column]["Lesser"]):
                lesser.append(column)
            if(univariate[column]["Max"]>univariate[column]["Greater"]):
                greater.append(column)
                return lesser,greater
    
    def descriptive_Analysis(self,dataset,quan):    
        univariate=pd.DataFrame(index=["Mean","Median","Mode","Min","25%","50%","75%","Max","IQR","1.5rule","Lesser","Greater","Variance","Std","Skew","Kurtosis"],columns=quan)

        for column in quan:
            print(column)
            univariate[column]["Mean"]=dataset[column].mean()
            univariate[column]["Median"]=dataset[column].median()
            univariate[column]["Mode"]=dataset[column].mode()[0]
            univariate[column]["Min"]=dataset[column].min()
            univariate[column]["25%"]=np.percentile(dataset[column],25)
            univariate[column]["50%"]=np.percentile(dataset[column],50)
            univariate[column]["75%"]=np.percentile(dataset[column],75)
            univariate[column]["Max"]=np.percentile(dataset[column],100)
            univariate[column]["IQR"]=univariate[column]["75%"]-univariate[column]["25%"]
            univariate[column]["1.5rule"]=1.5*univariate[column]["IQR"]
            univariate[column]["Lesser"]=univariate[column]["25%"]-univariate[column]["1.5rule"]
            univariate[column]["Greater"]=univariate[column]["75%"]+univariate[column]["1.5rule"]
            univariate[column]["Variance"]=dataset[column].var()
            univariate[column]["Std"]=dataset[column].std()
            univariate[column]["Skew"]=dataset[column].skew()
            univariate[column]["Kurtosis"]=dataset[column].kurtosis()
        return univariate
    
def get_pdf_probability(dataset,startrange,endrange):
    from matplotlib import pyplot
    from scipy.stats import norm
    import seaborn as sns
    ax = sns.distplot(dataset,kde=True,kde_kws={'color':'blue'},color='Green')
    pyplot.axvline(startrange,color='Red')
    pyplot.axvline(endrange,color='Red')
    sample = dataset
    sample_mean =sample.mean()
    sample_std = sample.std()
    print('Mean=%.3f, Standard Deviation=%.3f' % (sample_mean, sample_std))
    dist = norm(sample_mean, sample_std)
    values = [value for value in range(startrange, endrange)]
    probabilities = [dist.pdf(value) for value in values]    
    prob=sum(probabilities)
    print("The area between range({},{}):{}".format(startrange,endrange,sum(probabilities)))
    return prob
  

