#import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

def load_cluster(filename):
    #This function takes the name of the file as its argument and returns the saved model
    #remember to declare the file extension i.e. either .sav or .pkl
    clustering_model = pickle.load(open(filename, 'rb'))
    return clustering_model

def get_response(directory):
    user_reponse = pd.read_csv(directory)
    return user_reponse


#we want to know which personality cluster the User belongs too
def userPersonality_cluster():
    Personality_loaded = load_cluster(filename)
    user_response = get_response(filedirectory)
    user_personality = Personality_loaded.predict(user_response)
    print("User Personality class is ",user_personality)
    return user_personality

def Personality_sum():
    #converting the response to a list to identify the personality classes
    my_response = get_response(filedirectory)
    col_list = list(my_response)
    ext = col_list[0:10]
    est = col_list[10:20]
    agr = col_list[20:30]
    csn = col_list[30:40]
    opn = col_list[40:50]

    #Checking the personality class
    personality = userPersonality_cluster()
    
    #finding the average of each personality class
    df_sum = pd.DataFrame()
    df_sum['extroversion'] = my_response[ext].sum(axis=1)/10
    df_sum['neurotic'] = my_response[est].sum(axis=1)/10
    df_sum['agreeable'] = my_response[agr].sum(axis=1)/10
    df_sum['conscientious'] = my_response[csn].sum(axis=1)/10
    df_sum['open'] = my_response[opn].sum(axis=1)/10
    df_sum['cluster'] = personality #correct the name of this column

    """This section of the function outputs a graph showing the
        breakdown of the personality test"""
    df_sumCopy = df_sum.drop("cluster",axis=1)
    plt.bar(df_sumCopy.columns, df_sumCopy.iloc[0,:], color='green', alpha=0.2)
    plt.plot(df_sumCopy.columns, df_sumCopy.iloc[0,:], color='red')
    plt.title(personality)
    plt.xticks(rotation=45)
    plt.ylim(0,4);
    return df_sum