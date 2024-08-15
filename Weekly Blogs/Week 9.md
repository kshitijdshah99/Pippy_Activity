# Progress till Now📈
I am done with completing major part of the UI modification. I am also clear with major parts of the things with respect to integration. 

# Week 9
Thus, this week, I looked into further integration-related avenues. essentially installing models on servers, utilizing APIs, and so forth. For my friends, I would like it to be summarized in this blog post.
I have created an LLM RAG architecture in my Colab file, but it is obviously not server-scalable. 

## First Step 
Transform the Colab file into a requirements.txt file containing all of the dependencies in a.py file. This allows you to run an LLM locally on your Visual Studio code. A separate environment should be created for the same, and requirements.txt should have a list of all the dependencies. You can install all of the dependencies locally on your machine by using the command provided below.

```pip install -r requirements.txt```

## Step 2 
With this you would have been done with making the mode run locally. Now it's time to deploy it on the server. On deploying it to the server you can use 2 different ways.
1. Docker & Kubernetes🐳 
2. Using APIs

### Docker Utilization🐳 
Docker is a fantastic tool based on the containerization concept. The first step is to create a Docker file with a list of all the dependencies and code. The file is then created as a Docker image. You can drag and drop this image to wherever you need it. Indeed, the model would then be running on the server after it was withdrawn. 

### Advantages
1.When there would be several models running on a server there are chances of conflict arising out in the dependencies in that case docker and kubernets would prove beneficial to us.
2. Docker images can be easily deployed on aws and Microsoft azure servers making it easy for future use.
3. This would also incrrease the flexibility and the scalability of the model.

### Employing APIs
This is a straightforward and widely used process that involves downloading all dependencies from the server and contacting the LLM's API via **fastAPI or flask**. All we have to do is develop different code for the fastAPI.

**Which is preferable??**

Docker is my choice if everything is operating smoothly since it combines all dependencies into a single block, which makes it easier to deal with in the future. I assume that in the future, we'll be updating, altering, or replacing the LLM, and if dependencies are downloaded to the server, conflicts could arise throughout that process. I choose to use Docker in order to avoid this and to seek greater scalability and flexibility. My mentors have given me the go-ahead for the same.

I completed all of my research for this week in one go. Please let me know if you have any mistakes or recommendations. I'm up for recommendations. Aside from this, I successfully tried to run a model locally.

## Running Llama3 locally using Ollama
Firstly I pulled a Llama3 model of 8B parameters from Ollama. It had a size of 4.7GB hence I decided not to run it on the by local VM where Sugar was installed. I ran it on my Windows computer since I was afraid that this would cause my virtual machine to crash. I succeeded.

### Problems I Ran Into⚠
The sole problem with this local model was that it took several minutes to generate the code due to an excessively high latency time.

# Summary
This week I had completed my research on the integration techniques and it was a success. I was successful enough to run the Llama3 model locally on my Windows system.

# Plan for next week📝
I am planning to have a meet with Bernie so that I can understand what he is expecting and accordingly make changes in the model. Besides this I would be first try to integrate this model locally in the Pippy activity on my Virtual Machine.

