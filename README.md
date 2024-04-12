# Pippy_Activity🐍

## Introduction 📝
Our purpose of intgrating LLM in Pippy-Activity is quite clear. Making co-pilot quite similar like github but on a much elementary level and easy to use for children. Python codes which LLM generate are based mainly for developers to understand beacause its trained on a data of codes of developers available on internet. There are chances that the code generated by these models may be difficult for kids to understand beacause many a times kids are unable to give structured and clear prompts. This results in hallucinations in our output.
## Which LLMs to use❓
There are many FOSS LLM available in the market like **Gemini, codellama, Mistral, Llama, GPT2, Gemma, Bloom, Mixtral, Llama2 and much more.** Based on their performance and architecture we need to shortlist the LLM for code generation purpose.
While working with Gemini, Bloom, GPT2 I found they are great for general text generative tasks but not suitable for code generation purposes.
This is because
1. The models had many hallucinations while working on complex codes which involve good amount of logic.
2. Computational power consumption of these models is relatively high compared to other models for same tasks. This adds a lot of maintainance cost in future.
3. Difficulties in fine-tuning these models. Hence making it difficult for us to cater kids.

### Codellama
I personally feel this model quite relatable to our project. Being launched by Meta in correspondance to LLama2 specifically for code-generation and correction tasks. This itself prooves the efficiency of our model.        
Click [here](https://arxiv.org/pdf/2308.12950.pdf) to view the research paper based on codellama.
This is my final model using codellama which I have made reading the research paper and other resources(model used-[Codellama](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Pippy_Assistant_codeLlama.ipynb), [output of model](https://colab.research.google.com/drive/1sJ7WdnEkQHI-DCRmWQ12IFXgpDuT6hIJ#scrollTo=k_RJObixH_HR)).
This can be made to operate on CPU instead on GPUs because GPUs are expensive and not FOSS. Hence using codellama is a great alernative.
In above code there are 2 codellama models trained on 7B and 13B parameters. The 7B parameter model are relatively easy to fine-tuned and can be trained on our specific dataset using less GPU resources whereas the 13B model would require more computational power as it's fine-tuned on extra billions of parameters.
#### Outputs mentioned in Research paper
![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Research%20Paper%20output.png)
Yes, the output which model is generating is quite higher compares to the level which kids can understand. However I have solved this issue by setting agents or pre-defined system prompts in our model preventing all these hallucinations.




