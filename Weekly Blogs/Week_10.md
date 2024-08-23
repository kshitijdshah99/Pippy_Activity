# Progress till Now📈
Till now I was done running a LLM locally in my terminal. The Llama3.1 model was using streamlit as the UI. Now my task was to built a RAG version of the same model which I had built in google Colab. For experimental purpose I had built a simple LLM locally.

# Week 10
This week I built the identical RAG architecture, which I had made previously in my Colab file. The RAG model which I had built on colab was not suitable to be deployed on the server a .py file could only help the model run locally.

I used Llama3.1 and modified it's architecture such that it supports RAG. The accuracy was pretty good corresponding to the level of kids and it out performed most of LLMs in terms of accuracy. Llama3.1 was the latest and best open source model available in the market.

## Virtual Environment
Using Miniconda I built a virtual environment where all the dependencies of the LLM where installed this was done in order to prevent conflicts with the sugar code.

```
langchain
langchain-ollama
streamlit
langchain_experimental
faiss-cpu
```

These where some of the primary requirements to run model locally I made it sure that the model does not require a GPU to run because that's resource expensive. CPU's are capable to perform these computations.

## Additional Tasks
Ibaim gave me some important task of testing and verifying the modified files on the Sugar codebase. My task was to test them and give him the report. Due to college work this issue got delayed which I would be starting with the next week. Here's the link for the same- https://github.com/sugarlabs/sugar/pull/988#issuecomment-2296894738

# Summary
This week I developed RAG model in Llama3.1 locally with all it's dependencies in the virtual environment which was previously developed on Google colab.

# Plan for next week📝
Next week I would be starting to work on the integration part and also the issue which Ibiam had addressed me.


