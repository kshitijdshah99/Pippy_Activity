# Progress till Now📈
Up until week 2, I had completed the implementation of a model that could create Python code for children while also correcting them as needed. Last week, I encountered a major difficulty with training and loading Large Language Models, prompting me to modify my strategy from fine-tuning to a RAG-based approach.

# Week 3
This week, I spent the most of my time looking for adequate pygame documentation that included all of the intricacies and functionality of the methods utilized in this Python module. When it comes to functional use cases, Pygame is a somewhat large Python package. This makes it useful for a wide range of tasks and activities.
Sugar's codebase is entirely composed of Python and Sugar GTK code, with Pygame serving as its basis. Recently developed Sugar activities are mostly designed with Pygame.
## So what exactly is RAG?
RAG stands for retrieval-augmented generation. To put it simply, LLMs are trained on current data, hence the models are frequently out of date with the latest market information. It is evident that current data is always being updated, thus to avoid data loss, LLMs are kept up to date utilizing the RAG technique. In the RAG approach, our model first checks the user's query. In our case, once the child's query has been processed, it first checks in the knowledge database or the context that we have provided to the model in the retrieved part. If an answer to the query is found there, the output is directly generated based on that context; otherwise, the LLM generates an answer based on the data on which it has been trained.

### How did I install the RAG? 
So, RAG is essentially a method that can be included into any LLM. It may be used with a variety of frameworks Langchain is one of the most common options. I used langchain to create one. In the langchain framework, I tested pypdf, a Python package for splitting, merging, cropping, and modifying PDF documents. This library assisted me in reading the pdf and extracting all of the relevant information. This material was then tokenized and used as context throughout the retrieval process.

## Dataset
This is the [document](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Pygame%20Documentation.pdf) I discovered on the internet. It's pretty descriptive, but I altered it to meet the requirements.

### This documentation covers several ideas, to summarize them:

1.**Basic principles** taught were pygame introduction, dealing with shapes, pictures, text, and drawing graphics primitives.

2.**Intermediate techniques** included playing music and constructing a graphic user interface (GUI).

3.**Advanced notions** include creating an app, a basic board game, or even tiles for it.

### Reasons why I chose this documentation❓
1. It includes correct code samples.
The manual includes code snippets and examples for all of the basic to complex functions mentioned. This makes it easier for the LLM to create the appropriate output relating to the child's question.
2. Well-formatted data.
Everything in this handbook has been presented in an organized manner, allowing LLM to easily process the child's query and produce a proper response. This thorough manual strives to cover every feature of the Pygame library.

## Ouput

# Summary

# Plan for next week
