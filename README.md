# Final Evaluation Report for Google Summer of Code'24

<div align="center">
<img src="https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Output/GSoC%40Sugarlabs.png" alt="drawing" width="900"/>
</div> 


## Details

|  |  |
| --- | --- |
| Name | [Kshitij Shah](https://github.com/kshitijdshah99) |
| Organisation | [Sugarlabs](https://github.com/sugarlabs) |
| Mentor | [Walter Bender](https://github.com/walterbender), [Ibiam Chihurumnaya](https://github.com/chimosky), [Perrie]()|
| Project | [Add an AI-assistant to the Pippy Activity](https://summerofcode.withgoogle.com/archive/2024/projects/lccFY8AH) |

## Table of Contents

1. [Project Description](#project-description)
2. [GSoC plan](#gsoc-journey)
3. [Work Accomplished](#work-accomplished)
   - [New Operator Implementations](#1-implementing-New-Operator-Classes)
   - [Extending Existing Operators](#2-adapting-existing-operator-classes-to-parse-parameterized-shapes)
4. [Challenges and Learning Outcomes](#challenges-and-learning-outcomes)
5. [Future Plans](#future-plans)
6. [Conclusion](#conclusion)

## Project Description

Pippy is the Sugar "learn to program in Python" activity. It comes with lots of examples and has sufficient scaffolding such that a learner could modify an existing Sugar activity or write a new one. The goal of this project is to add "co-pilot"-like assistance to Pippy. A learner should be able to ask the AI to provide example Python code to help them navigate the language and explore possibilities in a more open way than the collection of Pippy examples affords. Besides correcting code and providing example to kids the project aims to help developers navigate through Sugar-toolkit and also GTK basics helping them contribute in more effective way. Our AI-assistant model would provide contributors sufficient examples to understand how the sugar codebase works.

## GSoC Journey
This was the first time ever when Sugarlabs started integrating AI in their activities. Hence they developed a new repo in their organisation named [sugar-ai](https://github.com/sugarlabs/sugar-ai) to keep track of all of their AI-models. I consider myself fortunate to be one of the first member and contributor of sugar-ai.
To proceed with the developments of AI models and integrating in Sugar activities mainly involves 4 different phases of development, which are as follows.

 **1. <ins> Development of the AI-model </ins>** 

This phase was the core of the entire project, focusing on the development of an AI-powered model designed to facilitate navigation through Python, GTK, and Pygame for both young learners and contributors to the Sugar codebase. To maximize usability, the model was integrated with a modified UI of the [Pippy Activity](https://github.com/sugarlabs/Pippy).

**2. <ins> Upgrading the UI of the existing activity <ins>**

The user interface of Pippy was enhanced to accommodate all the features of the Co-Pilot AI model. A major challenge in this phase was improving the UI while maintaining consistency with the existing Sugar design principles. 

**3. <ins> Integration using fastAPI <ins>**

The AI model operates in the backend and communicates with the frontend of Pippy via the FastAPI framework. A unified FastAPI-based backend was developed to integrate all AI-driven chatbots in sugar-ai, ensuring compatibility with their respective activities. 


**4. <ins> Deployment on AWS servers using Docker <ins>**

All AI models are deployed using Docker, ensuring a consistent and reproducible environment. The Docker image bundles all necessary dependencies, including the LLM (Large Language Model), making it easy to deploy and run the models seamlessly. This containerized approach enhances scalability, portability, and maintainability across different Activities in Sugar.

## Work Accomplished

I had started exploring sugar codebase and building sugar locally on my system. By the community bonding period I was well versed with my tasks and the flow of the entire project. During my community bonding period I had built few AI-workflows and had performed LLM inferencing on some of the FOSS models so as to evaluate the performance metrics. I had done most of the filtering of the AI-models by the 2nd week. I evaluted models based on number of parameters on which it has been trained, the size of the model, performance and flexibility it provided to intergrate with other frameworks(like RAG).



### 1. GenerativeAI model
- Ollama was a strong candidate for running models locally, as it provided a diverse set of FOSS (Free and Open Source Software) models, allowing us to experiment and select the most suitable ones. The Co-Pilot AI model was designed to effectively assist with Python, Pygame, and Sugar GTK, forming the foundation of the Sugar codebase.
- To enhance its performance, I began fine-tuning models from the LLaMA family on medium-sized datasets. However, the training process proved to be computationally intensive, exceeding the Colab GPU limits. This challenge led us to explore an alternative approach—Retrieval-Augmented Generation (RAG).
- Instead of relying solely on fine-tuned models, we implemented RAG (Retrieval-Augmented Generation) to dynamically fetch relevant context from Pygame and Sugar GTK documentation. This hybrid approach balanced computational efficiency while ensuring the AI model could provide more accurate and context-aware responses, improving both usability and performance.

| Pull Request             | PR Number                               |   Status  |
   |--------------------------|-----------------------------------------|-----------|
   | Pippy's AI-RAG model        | [#3](https://github.com/sugarlabs/sugar-ai/pull/3) | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |
   | Handling Sugar and LLM Dependencies |  [#4](https://github.com/sugarlabs/sugar-ai/pull/4) |  <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |
   | Removing deprecated version of Langchain | [#6](https://github.com/sugarlabs/sugar-ai/pull/6) | <img src="https://img.shields.io/badge/PR-Merged-blueviolet?style=for-the-badge&logo=appveyor"> |

   ### 2. Pippy's new look
  - One of the challenges I faced was learning GTK and modifying the UI, as my background was primarily in Large Language Models (LLMs) and Generative AI, with limited experience in frontend development. While it was difficult initially, the process became enjoyable as I gained more familiarity with GTK and UI design.
- As part of the UI enhancement, I also designed a custom AI-bot icon using Inkscape, which can be seen [here](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Output/Pippy's%20AI-assistant.svg).
- Currently, our primary focus remains on the AI integration, and the UI code is yet to be reviewed by the mentors. Further refinements will be made based on their feedback.be reviewed by the mentors.

| Commit          | Link                            |   Status  |
|--------------------------|-----------------------------------------|-----------|
| Modified Pippy Activity        | [Code](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Ollama%20Running%20Model%20locally/Pippy_With_Integration_v2.py) |<img src="https://img.shields.io/badge/PR-Yet_To_Be_Raised-green?style=for-the-badge&logo=appveyor"> |

   ### 3. FastAPI Integration
   This was a very new concept of handling cross platform dependencies and something which I loved the most in my entire project.
 



## Challenges and Learning Outcomes




## Future plans


## Conclusion


