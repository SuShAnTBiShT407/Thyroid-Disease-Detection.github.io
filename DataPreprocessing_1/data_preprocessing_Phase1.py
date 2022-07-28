import pandas as pd
import numpy as np
from application_logger.application_logger import App_Logger

class data_preprocessing_phase_first:
    def __init__(self) -> None:
        self.pd = pd
        self.logger = App_Logger()

    def ReadData(self, path):
        log_file = open("Training_Logs/data_preprocessing_phase_1_logger.txt", "a+")
        try:
            self.logger.log(log_file, "Reading dataset........")
            df = self.pd.read_csv(path)
            self.logger.log(log_file, "read dataset successfully !")
            return df
        except:
            self.logger.log(log_file, "Error while reading dataset")

    def LabelColumnOperation(self, df):
        log_file = open("Training_Logs/data_preprocessing_phase_1_logger.txt", "a+")
        try:
            self.logger.INFO("Checking the columns of the dataset...")
            '''
            The diagnosis consists of a string of letters indicating diagnosed conditions. A diagnosis "-" indicates no condition requiring comment. A diagnosis of the form "X|Y" is interpreted as "consistent with X, but more likely Y". The conditions are divided into groups where each group corresponds to a class of comments.

            Letter    Diagnosis
            ------    ---------

            hyperthyroid conditions:

                A    hyperthyroid
                B    T3 toxic
                C    toxic goitre
                D    secondary toxic

            hypothyroid conditions:

                E    hypothyroid
                F    primary hypothyroid
                G    compensated hypothyroid
                H    secondary hypothyroid

            binding protein:

                I    increased binding protein
                J    decreased binding protein

            general health:

                K    concurrent non-thyroidal illness

            replacement therapy:

                L    consistent with replacement therapy
                M    underreplaced
                N    overreplaced

            antithyroid treatment:

                O    antithyroid drugs
                P    I131 treatment
                Q    surgery

            miscellaneous:

                R    discordant assay results
                S    elevated TBG
                T    elevated thyroid hormones
            '''
            self.logger.log(log_file, "Creating the new Label column as 'Outcome'....")
            df["outcome"] = df["-[840801013]"].str[0]
            self.logger.log(log_file, "Delete the existing Label column named as -[840801013]")
            df.drop(["-[840801013]"], axis=1, inplace=True)
            self.logger.log(log_file, "Creating the diagnosis list ")
            diagnosis_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
            df["outcome"].replace(to_replace = diagnosis_list, value='yes', inplace=True)
            self.logger.log(log_file, "replaced all the disease all different catagory with one catagory 'Yes' ")
            df["outcome"].replace({"-":0, "yes":1}, inplace=True)
            self.logger.log(log_file, "Classified the Label feature into 0 and 1")
            return df
        except:
            self.logger.log(log_file, "Error while generalizing Label column ")
    
    def ColumnRenaming(self, df):
        log_file = open("Training_Logs/data_preprocessing_phase_1_logger.txt", "a+")
        try:
            self.logger.log(log_file, "Renaming the columns in dataset....................")
            df.rename(columns = {"29":"age", "F":"sex", "f":"thyroxine", "f.1":"query_thyroxine", "f.2":"antithyroid", "f.3":"sick",
            "f.4":"pregnant", "f.5":"thyroid_surgery", "f.6":"I131 treatment", "t":"query_hypothyroid", "f.7":"query_hyperthyroid",
            "f.8":"lithium", "f.9":"goitre", "f.10":"tumor", "f.11":"hypopituitary", "f.12":"psych", "t.1":"TSH_measured",
            "0.3":"TSH", "f.13":"T3_measured", "?":"T3", "f.14":"TT4_measured","?.1":"TT4",
            "f.15":"T4U_measured", "?.2":"T4U", "f.16":"FTI_measured", "?.3":"FTI", "f.17":"TBG_measured",
            "?.4":"TBG", "other":"referral_source"}, inplace=True)
            self.logger.log(log_file, "Renamed all the columns in dataset!")
            return df
        except:
            self.logger.log(log_file, "Error while renaming the columns in dataset...!")
    def SaveCSVformat(self, df):
        log_file = open("Training_Logs/data_preprocessing_phase_1_logger.txt", "a+")
        try:
            self.logger.log(log_file, "Saving the file as a .csv file......")
            df.to_csv("Training_Dataset_phase1/train_data_phase_1.csv", index=False)
            self.logger.log(log_file, "Data Saved!")
        except:
            self.logger.log(log_file, "Error while saving the file!")    
