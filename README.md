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
2. [GSoC plan](#pippy-ai-assistant)
3. [Work Accomplished](#work-accomplished)
   - [New Operator Implementations](#1-implementing-New-Operator-Classes)
   - [Extending Existing Operators](#2-adapting-existing-operator-classes-to-parse-parameterized-shapes)
4. [Challenges and Learning Outcomes](#challenges-and-learning-outcomes)
5. [Future Plans](#future-plans)
6. [Conclusion](#conclusion)

## Project Description

Pippy is the Sugar "learn to program in Python" activity. It comes with lots of examples and has sufficient scaffolding such that a learner could modify an existing Sugar activity or write a new one. The goal of this project is to add "co-pilot"-like assistance to Pippy. A learner should be able to ask the AI to provide example Python code to help them navigate the language and explore possibilities in a more open way than the collection of Pippy examples affords. Besides correcting code and providing example to kids the project aims to help developers navigate through Sugar-toolkit and also GTK basics helping them contribute in more effective way. Our AI-assistant model would provide contributors sufficient examples to understand how the sugar codebase works.

## Pippy AI-assistant
To proceed with the developments of AI models and integrating in Sugar activities mainly involves 4 different phases of development, which are as follows.

**1. Development of the AI-model**

This phase was the core of the entire project, focusing on the development of an AI-powered model designed to facilitate navigation through Python, GTK, and Pygame for both young learners and contributors to the Sugar codebase. To maximize usability, the model was integrated with a modified UI of the [Pippy Activity](https://github.com/sugarlabs/Pippy).

**2. Upgrading the UI of the existing activity**

The user interface of Pippy was enhanced to accommodate all the features of the Co-Pilot AI model. A major challenge in this phase was improving the UI while maintaining consistency with the existing Sugar design principles. 

**3. Integration using fastAPI**

The AI model operates in the backend and communicates with the frontend of Pippy via the FastAPI framework. A unified FastAPI-based backend was developed to integrate all AI-driven chatbots in sugar-ai, ensuring compatibility with their respective activities. 


**4. Deployment on AWS servers using Docker**

All AI models are deployed using Docker, ensuring a consistent and reproducible environment. The Docker image bundles all necessary dependencies, including the LLM (Large Language Model), making it easy to deploy and run the models seamlessly. This containerized approach enhances scalability, portability, and maintainability across different Activities in Sugar.




## Work Accomplished


## Challenges and Learning Outcomes


## Future plans


## Conclusion


