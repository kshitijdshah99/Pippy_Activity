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
   - [1. GenerativeAI model](#1-generativeAI-model)
   - [2. Pippy's new look](#2.-pippy's-new-look)
   - [3. FastAPI Integration](#3.-fastapi-integration)
   - [4. Deployment using Docker](#4.-deployment-using-docker)
   - [5. Maintanence](#5.-maintanence)
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
| Modified Pippy Activity        | [Code](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Ollama%20Running%20Model%20locally/Pippy_With_Integration_v2.py) |<img src="https://img.shields.io/badge/PR-Yet_To_Be_Raised-orange?style=for-the-badge&logo=appveyor"> |

   ### 3. FastAPI Integration
   - One of the most exciting aspects of this project was handling cross-platform dependencies, a challenge I thoroughly enjoyed. Sugar operates on a somewhat deprecated Python version (around 3.10), whereas the AI models—leveraging LangChain, Transformers, and Ollama—require the latest Python versions to function properly. This version mismatch created a significant challenge, making it essential to use FastAPI for seamless communication between the backend (AI model) and the frontend (Pippy Activity).
   - As I progressed, I realized that my mentors’ primary motivation for using FastAPI was to create a microservices architecture that could support future AI model deployments on Sugar. These microservices would enable the deployment of AI models as Docker images hosted on AWS servers. By implementing multiple microservices for a single Docker image, we could significantly enhance resource reusability, ensuring a scalable and efficient infrastructure for upcoming AI-driven activities in the Sugar ecosystem.

| Pull Request             | PR Number                               |   Status  |
   |--------------------------|-----------------------------------------|-----------|
   | FastAPI implementation        | [#12](https://github.com/sugarlabs/sugar-ai/pull/12) | <img src="https://img.shields.io/badge/PR-Yet_To_Be_Reviewed-green?style=for-the-badge&logo=appveyor"> |

 ### 4. Deployment using Docker 
Currently, work is still in progress on this phase of the project. We are encountering several challenges, including:
1. Dependency Conflicts – Managing compatibility between different Python versions and libraries used in Sugar and the AI models.
2. Large Docker Image Size – Optimizing the Docker image to reduce its size while maintaining all necessary dependencies.
3. Migration from Ollama to Hugging Face – Transitioning to Hugging Face models for better flexibility, community support, and improved model performance.

### 5. Maintanence
- Since Sugar-AI is a new platform for AI model development, there are many aspects that need careful consideration and refinement. Currently, I am actively engaged in resolving issues raised by contributors to ensure a smooth development process.

| Pull Request             | PR Number                               |   Status  |
   |--------------------------|-----------------------------------------|-----------|
   | Error Handling      | [#11](https://github.com/sugarlabs/sugar-ai/pull/11) | <img src="https://img.shields.io/badge/PR-closed-red?style=for-the-badge&logo=appveyor"> |
   | Dependency Handling     | [#8](https://github.com/sugarlabs/sugar-ai/pull/8) | <img src="https://img.shields.io/badge/PR-Open-blue?style=for-the-badge&logo=appveyor"> |
   | Migrating to HuggingFace     | [#14](https://github.com/sugarlabs/sugar-ai/pull/14) | <img src="https://img.shields.io/badge/PR-Open-blue?style=for-the-badge&logo=appveyor"> |
   
- At the same time, I am working on documenting key aspects of the Sugar-AI repository, making it easier for future contributors to understand and contribute effectively. This documentation will serve as a foundation for maintaining and expanding the AI ecosystem within Sugar.

| Pull Request             | PR Number                               |   Status  |
   |--------------------------|-----------------------------------------|-----------|
   | Adding README for sugar-ai | [#16](https://github.com/sugarlabs/sugar-ai/pull/16) | <img src="https://img.shields.io/badge/PR-Yet_To_Be_Reviewed-green?style=for-the-badge&logo=appveyor"> |

## Challenges and Learning Outcomes






## Future plans


## Conclusion


