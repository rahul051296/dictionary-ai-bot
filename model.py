from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from pprint import pprint

def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUConfig(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'wordsnlu')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/wordsnlu', RasaNLUConfig('config_spacy.json'))
	pprint(interpreter.parse("what is the meaning of donkey"))
	
if __name__ == '__main__':
	train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	#run_nlu()