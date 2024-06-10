# Google Summer Of Code'24 Starts
In the pre-GSoC and community bonding period I understood orgs mission, goal and the style of operation. I got familiar with the Sugar desktop environment and also what I have to do in my project for this summer. **My task was to Add an AI-assistant to Pippy activity in Sugar.**

### Tasks performed during this period:
1. Setup Sugar environment locally
2. Try out different LLMs
3. Decide the LLM Architecture
3. Finalise workflow
4. Communicated with my peers

#### Setup Sugar environment locally
Sugar is a desktop environment built for kids. To explore the different activities within it I decided to setup locally. I used packed sugar to try out differnet activities.

#### Try out different LLMs
This project involves code generation hence it opens up lots of opportunity for different LLMs to work with. I tried out various open-source models because sugarlabs supports FOSS only. Some of the LLMs which I tried were LLama2, Gemini, codellama, mistral, bloom, Llama2, GPT2 and many more. I have shared some of these codes in this repository for reference. 

#### Decide the LLM Architecture
We can enhance productivity of above stated LLMs using many approaches like fine-tuning, rag approach, prompting and using agents. On experimenting out these architectures I found fine-tuning and rag approach is the best.

#### Finalise workflow
Once model and architecture were short listed based on their performance metrics I started finalising the workflow for the AI part of this project.

#### Communication with my peers
This was one of the most intresting part of community bonding period. I discussed with my mates working on their AI based projects for GSoC and DMP at Sugarlabs. They brought a lots of LLM knowledge on board. For chatbot related projects fine-tuning prooved quite good. Music-blocks a part of sugarlabs had many AI projects. Many of them used LLama3 model because of it's testing parameters reaching level upto that of openAI's GPT4. Llama3 was recently released in the open-source market.
 
# Week 1 
By this time I had shortlisted following models
1. Codellama
2. LLama3
3. Llama2
   
These models generated code upto my expectation and they also corrosponded to the kids coding skills. This made me select these models.
Here are the outputs for the different models I tried out.

## Codellama
This model has many variants and just like Llama family there is an absolute family for Codellama2 models trained on different number of parameters and one special for Python languages. I selected the model having 7B parameters as it has less parameters and easy for computation purposes.

![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Pippy's%20AI-assistant%20output.png)

## Llama3
Latest model of the Llama family as of now with best accuracy. Besides providing the code it's efficient in giving examples with proper theoretical context of information as shown below.

![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/LLama3output.png)

## Llama2
I have used this model with RAG approach having a python slicing example and the output its generating corresponds exactly to the context provided in the pdf.
Here's the ouptut.

![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/LLama2output.jpeg)

## Summary 
In this week I have shortlisted models and various techniques I am going to be using for generating code. 
Our AI-assistant is mainly going to perform these 4 tasks:
1. Python code and example generation
2. Correcting codes written by kids
3. Generating code using pygame library
4. Help navigate through the GTK basics
   
Out of these 4 I have properly implemented the first and second part.


## Plan for next week
My goal for 2nd week is to 
1. Enhance the already implemented python code correction by fine-tuning it on some dataset, if required.
2. The following week I am going to try collect various codes from different activities in Sugar desktop. Based on these codes I would be fine-tuning the shortlisted model as possible and experimenting the accuracy. If fine-tuning does not work then would use a RAG based approach towards this.




