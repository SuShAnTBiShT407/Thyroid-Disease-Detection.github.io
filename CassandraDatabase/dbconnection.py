from application_logger.application_logger import App_Logger
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os 
import shutil
import pandas as pd
from os import listdir

class dbOperations:

    def __init__(self):
        self.path = 'Training_Dataset/'
        self.badFilePath = "Training_Raw_files_validated/Bad_Raw"
        self.goodFilePath = "Training_Raw_files_validated/Good_Raw"
        self.logger = App_Logger()
        self.secure_connect_bundle = 'secure-connect-ineuron.zip'
        self.client_id = 'eikKWhCUHTOlqOmqEDsXxsYw'
        self.client_secret = 'ZQlmtnLn6bYhw00E5bflReYpQpZuFdhfEjc8jT1ZrRuvmh3YjN38pEZGbthxlvEo12sgtj6-.sYCOy9-NvY6grTzEBUoghMbLl8a_agxrAObqpOzm4EG+GIpsfrf7yx0'

    def dataBaseConnection(self):

        """
                Method Name: dataBaseConnection
                Description: This method creates the database with the given name and if Database already exists then opens the connection to the DB.
                Output: Connection to the DB
                On Failure: Raise ConnectionError
                """
        try:
            cloud_config = {'secure_connect_bundle': self.secure_connect_bundle}

            auth_provider = PlainTextAuthProvider(self.client_id, self.client_secret)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            row = session.execute("select release_version from system.local").one()

            file = open("Training_Logs/CassandraConnectionLog.txt", 'a+')
            self.logger.log(file, "Cassandra database connection successful")
            file.close()
        except ConnectionError:
            file = open("Training_Logs/CassandraConnectionLog.txt", 'a+')
            self.logger.log(file, "Error while connecting to database: %s" % ConnectionError)
            file.close()
            raise ConnectionError

        return  session
    
    def createTableDb(self):
        """
                        Method Name: createTableDb
                        Description: This method creates a table in the given database which will be used to insert the Good data after raw data validation.
                        Output: None
                        On Failure: Raise Exception
                        """
        try:

            session = self.dataBaseConnection()
            try:
                integer = 'int'
                var = 'varchar'
                age = 'age'
                sex = 'sex'
                thyroxine = 'thyroxine'
                query_thyroxine = 'query_thyroxine'
                antithyroid = 'antithyroid'
                sick = 'sick'
                pregnant = 'pregnant'
                thyroid_surgery = 'thyroid_surgery'
                I131_treatment = 'I131_treatment'
                query_hypothyroid = 'query_hypothyroid'
                query_hyperthyroid = 'query_hyperthyroid'
                lithium = 'lithium'
                goitre = 'goitre'
                tumor = 'tumor'
                hypopituitary = 'hypopituitary'
                psych = 'psych'
                TSH_measured = 'TSH_measured'
                TSH = 'TSH'
                T3_measured = 'T3_measured'
                T3 = 'T3'
                TT4_measured = 'TT4_measured'
                TT4 = 'TT4'
                T4U_measured = 'T4U_measured'
                T4U = 'T4U'
                FTI_measured = 'FTI_measured'
                FTI = 'FTI'
                TBG_measured = 'TBG_measured'
                TBG = 'TBG'
                referral_source = 'referral_source'
                output = 'output'

                session.execute(f"CREATE TABLE db.Good_Raw_Data({age} {integer} PRIMARY KEY, {sex} {var}, {thyroxine} {var},{query_thyroxine} {var},{antithyroid} {var},{sick} {var},{pregnant} {var},{thyroid_surgery} {var}, {I131_treatment} {var}, {query_hypothyroid} {var}, {query_hyperthyroid} {var}, {lithium} {var}, {goitre} {var}, {tumor} {var}, {hypopituitary} {var}, {psych} {var}, {TSH_measured} {var}, {TSH} {var}, {T3_measured} {var}, {T3} {var}, {TT4_measured} {var}, {TT4} {var}, {T4U_measured} {var}, {T4U} {var}, {FTI_measured} {var}, {FTI} {var}, {TBG_measured} {var}, {TBG} {var}, {referral_source} {var}, {output} {var});")
                file = open("Training_Logs/CassandraTableLog.txt", 'a+')
                self.logger.log(file, "Tables created successfully!!")
                self.logger.log(file, "Database closed successfully")
                session.shutdown()
                file.close()
            except:
                file = open("Training_Logs/CassandraTableLog.txt", 'a+')
                self.logger.log(file, "Table already present in database")
                self.logger.log(file, "Database closed successfully")
                session.shutdown()
                file.close()

        except Exception as e:
            file = open("Training_Logs/CassandraTableLog.txt", 'a+')
            self.logger.log(file, "Error while creating table: %s " % e)
            file.close()
            file = open("Training_Logs/CassandraTableLog.txt", 'a+')
            self.logger.log(file, "Database closed successfully")
            session.shutdown()
            file.close()
            raise e

    def insertIntoTableGoodData(self):

        """
                               Method Name: insertIntoTableGoodData
                               Description: This method inserts the Good data files from the Good_Raw folder into the
                                            above created table.
                               Output: None
                               On Failure: Raise Exception
        """

        session = self.dataBaseConnection()
        goodFilePath = self.goodFilePath
        badFilePath = self.badFilePath
        onlyfiles = [f for f in listdir(goodFilePath)]
        log_file = open("Training_Logs/CassandraInsertionLog.txt", 'a+')

        age = 'age'
        sex = 'sex'
        thyroxine = 'thyroxine'
        query_thyroxine = 'query_thyroxine'
        antithyroid = 'antithyroid'
        sick = 'sick'
        pregnant = 'pregnant'
        thyroid_surgery = 'thyroid_surgery'
        I131_treatment = 'I131_treatment'
        query_hypothyroid = 'query_hypothyroid'
        query_hyperthyroid = 'query_hyperthyroid'
        lithium = 'lithium'
        goitre = 'goitre'
        tumor = 'tumor'
        hypopituitary = 'hypopituitary'
        psych = 'psych'
        TSH_measured = 'TSH_measured'
        TSH = 'TSH'
        T3_measured = 'T3_measured'
        T3 = 'T3'
        TT4_measured = 'TT4_measured'
        TT4 = 'TT4'
        T4U_measured = 'T4U_measured'
        T4U = 'T4U'
        FTI_measured = 'FTI_measured'
        FTI = 'FTI'
        TBG_measured = 'TBG_measured'
        TBG = 'TBG'
        referral_source = 'referral_source'
        output = 'output'

        for file in onlyfiles:
            try:
                data = pd.read_csv(goodFilePath + '/' + file)
                for i, row in data.iterrows():

                    query = f"insert into db.Good_Raw_Data ({age}, {sex}, {thyroxine}, {query_thyroxine}, {antithyroid}, {sick}, {pregnant}, {thyroid_surgery}, {I131_treatment}, {query_hypothyroid},{query_hyperthyroid}, {lithium}, {goitre}, {tumor}, {hypopituitary},{psych}, {TSH_measured}, {TSH}, {T3_measured}, {T3}, {TT4_measured}, {TT4}, {T4U_measured}, {T4U},{FTI_measured}, {FTI}, {TBG_measured}, {TBG},{referral_source}, {output}) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    try:
                        session.execute(query, tuple(row))
                        self.logger.log(log_file, " %s: File loaded successfully!!" % file)

                    except Exception as e:
                        raise e

            except Exception as e:
                self.logger.log(log_file, "Error while inserting data into table: %s " % e)
                shutil.move(goodFilePath + '/' + file, badFilePath)
                self.logger.log(log_file, "File Moved Successfully %s" % file)
                log_file.close()
                session.shutdown()

        session.shutdown()
        log_file.close()
    
    def selectingDatafromtableintocsv(self):

        """
                               Method Name: selectingDatafromtableintocsv
                               Description: This method exports the data in GoodData table as a CSV file. in a given
                                            location.
                               Output: None
                               On Failure: Raise Exception
        """

        self.fileFromDb = 'Training_FileFromDB/'
        self.fileName = 'InputFile.csv'
        log_file = open("Training_Logs/ExportToCsv.txt", 'a+')
        try:
            session = self.dataBaseConnection()

            main_list = []
            for i in session.execute("select * from db.Good_Raw_Data;"):
                main_list.append(i)

            # Make the CSV ouput directory.
            
            if not os.path.isdir(self.fileFromDb):
                os.makedirs(self.fileFromDb)

            # converting main_list to data frame
            df = pd.DataFrame(main_list)

            # saving the data frame df to output directory

            df.to_csv(f"{self.fileFromDb}" + '//' + f"{self.fileName}", index=False)

            self.logger.log(log_file, "File exported successfully!!!")
            log_file.close()

        except Exception as e:
            self.logger.log(log_file, "File exporting failed. Error : %s" % e)
            log_file.close()

    def TurncateTable(self):
        """
                               Method Name: TurncateTable
                               Description: This method delete the data in GoodData table. 
                               Output: None
                               On Failure: Raise Exception
        """
        
        
         
        try:
            session = self.dataBaseConnection()
            session.execute("TRUNCATE TABLE db.Good_Raw_Data;")
            
            file = open("Training_Logs/CassandraTableLog.txt", 'a+')
            self.logger.log(file, "Tables turncated successfully!!")
            file.close()
            session.shutdown()
            
        except Exception as e:
             file = open("Training_Logs/CassandraTableLog.txt", 'a+')
             self.logger.log(file, "Table Turncate failed. Error : %s" % e)
             file.close()
             session.shutdown()