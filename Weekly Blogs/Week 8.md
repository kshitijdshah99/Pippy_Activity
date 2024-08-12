# Progress till Now📈
Last I had implemented the basic layout of the chat window after which Walter advised me to do some changes in that which I made. 

# Week 8
This week I started with solving 2 problems which Walter had mentioned to me in the meet. They where basically related to the auto-deletion of chat messages and the Copy-paste feature.

## Issue 1
Initially I had implemented a mechanism where the chat messages would have disappeared once the child closes the chat window. Instead Walter advised me to modify this mechanism by saving the messages 
temporarily and clearing them once the child has exited Pippy acitvity. This was done bcz it was not feasible to store so many chats on the server, as Walter had mentioned.
I did it by making a temporary array which would store string of the messages of the kid. It would remain intact in the window until the child does not exit Pippy.

## Issue 2 
Second issue addressed to me was that the text in the message bubbles where not being able to be copy-paste. Hence I modified the code such that the kid can select the text from chat-window to terminal and 
vice versa.

## Integration
I started exploring different techniques using which I could integrate the AI-assistant to the modified UI. I started exploring integration techniques side by side enhancing UI because the UI was now capable enough 
that it could be integrated with the LLM.

Various steps to Integrate the AI-model

1. Running a model locally
2. Using Containerization techniques to make a docker file for that model locally
3. Downloading all the dependencies and bundling them up
4. Pulling the docker image for deploying the model on the server

I started exploring all these topics and held meets with Qixiang Wang to share ideas about containerization.

# Summary
This week I worked parallely on the UI as well as understanding the basic concepts useful in deploying the model. I still am exploring the docker part of the integration process. I've tried to enhance the UI
as much as possible, however I am still consistent in upgrading it.

# Plan for next week📝
By next Week I am planning to make a random model run locally, then I would be deploying this model on the Pippy's UI if it works out then I would be **deploying the actual RAG model which I had made.**
Besides this I assume I would be making modifications in the based on the mentors feedback in the weekly meeting.





