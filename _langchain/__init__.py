from utils import init_llm_chain
from templates import SHORT_ANSWER, LONG_ANSWER, LETTER_ANSWER
from models import Template
from common import set_env


test = """
Question #1 
Topic
A company manages capital equipment for an electric utility company: The company has a SQL Server database that contains maintenance records for the equipment:    
Technicians who service the equipment use the Dynamics 365 Field Service mobile app on tablet devices to view scheduled assignments. Technicians use a canvas app  
to display the maintenance history for each piece of equipment
update the history:
Managers use a Power Bl dashboard that displays Dynamics 365 Field Service and real-time maintenance data.
Due to increasing demand, managers must be able to work in the field as technicians
You need to design a solution that allows the managers to work from one single screen:
What should you do?
A. Add the maintenance
app to the Field Service Mobile app.
B. Add the manager Power Bl dashboard to the Field Service mobile app:
C. Create a new maintenance canvas app from within the Power Bl management dashboard:
D. Add the maintenance history app to the Power Bl dashboard.
Reveal Solution
Discussion
and
history

"""

set_env()
answer_template = Template(**SHORT_ANSWER)
answer_chain = init_llm_chain(answer_template.text, answer_template.input_variables, 0, 'correct_option_letter')
response = answer_chain.run(extracted_text=test)
print(response)