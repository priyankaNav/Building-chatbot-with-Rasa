from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

import warnings
import ruamel
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/assignment_rest_nlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-370742750130-370046925808-466090237687-d440c0bf52ae7861aa5e37b691c57367', #app verification token
							'xoxb-370742750130-464300796592-OPhQ9iyfTyTnCllfxrc1F1yj', # bot verification token
							'L8vVs6fdHLogBD9nZh3weKFE', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))