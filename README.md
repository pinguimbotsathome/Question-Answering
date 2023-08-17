# Question-Answering
Context based Question Answering using Generative QA.

## Tested
- **Transformers from Hugging Face**
	- multiple models -> they can be found at their website
	- supports multiple types of QA building
	- fast
	- efficient
	- Website: https://huggingface.co/
	- Code source: https://github.com/huggingface/transformers
- **haystack by deepset**
	- LLM(Large Language Models)
	- multiple ways to build a QA system
	- BERT models
		- you can finetune models
	- extensive documentation
	- efficient
	- heavy
	- multiple answers based on given texts
	- Website for haystack: https://haystack.deepset.ai/
	- Tutorials: https://haystack.deepset.ai/tutorials
	- Deepset website: https://www.deepset.ai/
	- Source: https://github.com/deepset-ai/haystack
- **Deeppavlov**
	- russian/en
	- 2 en only models
		- squad_bert
		- qa_squard2_bert
	- simple
	- efficient
	- based on transformers
	- Source code: https://github.com/deeppavlov/DeepPavlov
## Run
```bash
$ pip install -r requirements.txt
$ git clone https://github.com/pinguimbotsathome/Question-Answering
$ cd Question-Answering
$ python qa.py "question"
```
### Notes
Only outputs short answers.
