# Progress till Now📈
Last week, I finished integrating all of the functionality in our co-pilot model. Although the models were accurate, I wanted to eliminate hallucinations as much as possible. 
My mentor Walter suggested starting with UI and then improving efficiency of the LLMs.

# Week 5
I was bit confused in the start of this week on what to include as a part of Sugar-activities hence my mentor Ibiam advised me to make a new documentation for Sugar activities
this documentation would contain all the releveant content related to sugar-activities.

Once the documentation was done I shifted my focus in developing the figma design of the Sugar UI. This design included all the stuff like position of chatbox on the toolbox, it's color, font, name, symbol, window space and also a proper chat interface.


### Dataset🔗
Ibaim suggested that some of these topics be added in the revised documentation.

**1. Hello-World activity**
   
   Ofcourse Sugar has a lot of activities, therefore their codebase and logic are rather complicated for the model to grasp.
   To address this issue, I inserted the Hello-World activity, which is a basic activity in Sugar. It's built with Python GTK3+.
   It provided a clear example for users to understand how GTK is an integral part of the Sugar-codebase.
   
   Here's the Repo link for the same - https://github.com/sugarlabs/hello-world

**2. Sugar Toolkit GTK3+**

   This is essentially a website dedicated to studying the Sugar toolkit GTK3+. This is the most important and fundamental building component for developing Sugar activities.
   So from here I basically fetched stuff that was frequently used in contributing to Sugar. sugar3.activity.widgets is one of them that I have included in my documentation 
   because of it's high usage.

   This is the website link for the same - https://developer.sugarlabs.org/sugar3

**This is the link to the final documentation which is going to be loaded in the RAG model.**


## Pippy's new look🐍
Yes, with the integration of a large language model in Pippy, it's existing UI needed to be upgraded. I experimented with several figma designs, which are most comfortable for kids to work with while they are coding in Pippy. At the same time, I needed to maintain the UI of chatbots uniform throughout Sugar, so my efforts were focused there as well. 

**This is the link to the Figma design of the updated Pippy**


###  Figma design of Pippy


# Summary
With the complete of developing an AI-model we have started building the UI of Pippy where the LLM is going to be integrated.

To sumarize this week I performed 2 tasks
1. Built a documentation for Sugar-activities
2. Developed a rough figma design of the Pippy

Once the design is approved by the mentors I will start modifying the UI as per our needs.

# Plan for next week📝
Next week, I'll set up the environment appropriately using packed sugar. This is the local system that I will be utilizing to contribute to Sugar. Actually, I had previously set up the desktop environment, but it had some issues (the RAM assigned to the VM was limited, resulting in latency). This would require installing Sugar and obtaining tools such as VS Code and Zephyr to contribute to the codebase. 

Besides this I would be understanding the repo and file structure of Pippy-activity as it's bit complex to understand how the file are inter-related to each other.



   



