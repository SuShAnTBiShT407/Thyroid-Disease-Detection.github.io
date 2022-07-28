from cv2 import log
from application_logger.application_logger import App_Logger
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.decomposition import PCA

class Data_Preprocessing_Phase:
    def __init__(self):
        self.pd = pd
        self.logger  = App_Logger()
        self.pca = PCA(n_components=20)
        self.minmaxscaler = MinMaxScaler()
        self.sc = StandardScaler()
    
    def Read_preprocessed_Data(self):
        log_file = open("Training_Logs/data_preprocessing_phase_2_logger.txt", "a+")
        try:
            self.logger.log(log_file, "Reading Dataset.........")
            df = self.pd.read_csv("Training_Dataset_phase1/train_data_phase_1.csv")
            self.logger.log(log_file, "Read Data successfully!")
            return df
        except:
            self.logger.log(log_file, "Error occured while reading the file!")

    def ReplaceMissingValues(self, df):
        log_file = open("Training_Logs/data_preprocessing_phase_2_logger.txt", "a+")
        try:
            df.replace({"?": np.nan}, inplace=True)
            self.logger.log(log_file, "Replaced all '?' with NAN.")
            self.logger.log(log_file, "T3 and TBG have highest number of null values.")
            df.drop(["T3", "TBG"], axis=1, inplace=True)
            self.logger.log(log_file, "Drop T3, TBG, sex")
            df["sex"].fillna("unknown", inplace=True)
            self.logger.log(log_file, "Converting TSH, TT4, T4U, FTI as numeric column")
            df.TSH = pd.to_numeric(df.TSH)
            df.TT4 = pd.to_numeric(df.TT4)
            df.T4U = pd.to_numeric(df.T4U)
            df.FTI = pd.to_numeric(df.FTI)
            self.logger.log(log_file, "Removing the outliers...")
            index_age = df[df["age"]>100].index
            df.drop(index=index_age, inplace=True)
            index_tsh = df[df["TSH"]>15].index
            df.drop(index=index_tsh, inplace=True)
            self.logger.log(log_file, "We have droped the outliers from age and TSH columns!")
            self.logger.log(log_file, "filling the null values with mean......")
            df["TSH"] = df["TSH"].fillna(value=df["TSH"].mean())
            df["TT4"] = df["TT4"].fillna(value=df["TT4"].mean())
            df["T4U"] = df["T4U"].fillna(value=df["T4U"].mean())
            df["FTI"] = df["FTI"].fillna(value=df["FTI"].mean())
            self.logger.log(log_file, "Done filing the missing values with mean values")
            return df
        except:
            self.logger.log(log_file, "Error occured while handling missing values!!")

    def Encode_the_col(self, df):
        log_file = open("Training_Logs/data_preprocessing_phase_2_logger.txt", "a+")
        encode = LabelEncoder()
        try:
            self.logger.log("Encoding the column......")
            for i in df.columns:
                if df[i].dtypes == "object":
                    df[i] = encode.fit_transform(df[i])
            return df        
        except:
            self.logger.log(log_file, "Error while encoding the values !")

    def Seperate_the_dataset(self, df):
        log_file = open("Training_Logs/data_preprocessing_phase_2_logger.txt", "a+")
        try:
            self.logger.log(log_file, "Seperating the independent and dependent columns from dataset")
            x = df.iloc[:,:-1]
            y = df.iloc[:, -1]
            y.to_csv("Training_Dataset/y.csv")
            self.logger.log(log_file, "Saved the dependent columns as .csv file") 
            return x, y
        except:
            self.logger.log(log_file, "Error while seprating the independent and dependent columns")    


    def Multicollinearity(self, x):
        #scaler = StandardScaler()        
        log_file = open("Training_Logs/data_preprocessing_phase_2_logger.txt", "a+")
        try:
            self.logger.lof(log_file, "Appling Multicollinearity to my columns")
            #arr  = scaler.fit_transform(x)
            #return pd.DataFrame([[x.columns[i], variance_inflation_factor(arr, i)] for i in range(x.shape[1])], columns=["Features", "VIF"])
            x.drop(["T4U_measured", "FTI_measured", "TBG_measured","TT4_measured","TT4"], axis=1, inplace=True)
            self.logger.log(log_file, "Dropping the columns whose mulicollinearity is greater than 5!!")
            return x
        
        except:
            self.logger.log(log_file, "Error while finding Multicollinearity!!!")


    def Principal_Component_Analysis(self, x):
        log_file = open("Training_Logs/data_preprocessing_phase_2_logger.txt", "a+")
        try:
            x_transformed = self.sc.fit_transform(x)
            principal_col = self.pca.fit_transform(x_transformed)
            self.logger.log(log_file, "Creating DataFrame with Principal components")
            x_pca = pd.DataFrame(principal_col)
            self.logger.log(log_file, "Applying MinMaxScaler to each and every columns in the dataset")
            for i in x_pca.columns:
                x_pca[i] = self.minmaxscaler.fit_transform(x_pca[[i]])
            x_pca.to_csv("Training_Dataset/principaled_dataset.csv")
            self.logger.log(log_file, "Saved dataset after applying Principal component analysis!")
            return x_pca
        except:
            self.logger.log("Error while doing Principal Component Analysis!")            
            

    def Principal_Component_Analysis_TestData(self, x):
        #log_file = open("Training_Logs/data_preprocessing_phase_2_logger.txt", "a+")
        try:
            x_transformed = self.sc.fit_transform(x)
            arr = self.pca.transform(x_transformed)
            arr = self.minmaxscaler.transform(arr)
            return arr
        except:
            #self.logger.log(log_file, "Error in applying pca to test data!!")    
            pass

    