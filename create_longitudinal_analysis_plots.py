import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_horizontal_bars(sql_query:str,fig_name:str,shareyaxis:bool=False):
      connection = sqlite3.connect("data/kaggle_survey.db")
      response_counts = pd.read_sql(sql_query,con=connection)
      connection.close()
      fig,axes = plt.subplots(ncols=3,figsize=(32,8),sharey=shareyaxis) #ncols:水平排列的軸物件
      survey_years = [2020,2021,2022]
      for i in range(len(survey_years)):
          survey_year = survey_years[i]
          response_counts_year = response_counts[response_counts["surveyed_in"] == survey_year]   
          y = response_counts_year["response"].values  
          width = response_counts_year["response_count"].values
          axes[i].barh(y,width)
          axes[i].set_title(f"{survey_year}")
      plt.tight_layout()   
      fig.savefig(f"{fig_name}.png") 

'''
Select the title most similar to your current role (or most recent title if retired)
從事資料科學工作的職缺抬頭(title)有哪些？
2020:Q5
2021:Q5
2022:Q23
'''
sql_query_1 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q5' AND surveyed_in IN (2020,2021)) OR
      (question_index = 'Q23' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
#plot_horizontal_bars(sql_query_1,"data_science_job_titles")

'''
Select any activities that make up an important part of your role at work
從事資料科學工作的日常內容是什麼？
2020:Q23
2021:Q24
2022:Q28
'''
sql_query_2 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q23' AND surveyed_in = 2020) OR
      (question_index = 'Q24' AND surveyed_in = 2021) OR
      (question_index = 'Q28' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
#plot_horizontal_bars(sql_query_2,"data_science_job_tasks",shareyaxis=True)

'''
What programming languages do you use on a regular basis?
想要從事資料科學工作，需要具備哪些技能與知識？（程式語言）
2020:Q7
2021:Q7
2022:Q12
'''
sql_query_3 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q7' AND surveyed_in IN (2020,2021)) OR
      (question_index = 'Q12' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
#plot_horizontal_bars(sql_query_3,"data_science_programming_languages")

'''
Which of the following big data products (relational databases, data warehouses, data lakes, or 
similar) do you use on a regular basis?
想要從事資料科學工作，需要具備哪些技能與知識？（資料庫）
2020:Q29A
2021:Q32A
2022:Q35
'''
sql_query_4 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q29A' AND surveyed_in = 2020) OR
      (question_index = 'Q32A' AND surveyed_in = 2021) OR
      (question_index = 'Q35' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
#plot_horizontal_bars(sql_query_4,"data_science_job_databases")

'''
What data visualization libraries or tools do you use on a regular basis?
想要從事資料科學工作，需要具備哪些技能與知識？（視覺化）
2020:Q14
2021:Q14
2022:Q15
'''
sql_query_5 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q14' AND surveyed_in IN (2020,2021)) OR
      (question_index = 'Q15' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
#plot_horizontal_bars(sql_query_5,"data_science_job_visualizations")

'''
Which of the following ML algorithms do you use on a regular basis?
想要從事資料科學工作，需要具備哪些技能與知識？（機器學習）
2020:Q17
2021:Q17
2022:Q18
'''
sql_query_6 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q17' AND surveyed_in IN (2020,2021)) OR
      (question_index = 'Q18' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
#plot_horizontal_bars(sql_query_6,"data_science_job_machine_learnings")
