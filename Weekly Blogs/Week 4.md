# Progress till Now📈
By the conclusion of Week 3, I had integrated pygame documentation into my RAG model, as well as the fundamentals of code correction and code generation.
Pygame was used to create the UI for Sugar activities, while GTK was utilized to customize the toolbar and other functions. 
GTK was a crucial feature of the Sugar codebase. As a result, I was looking for documentation about it at this point.

# Week 4
The majority of activities created in Sugar nowadays make use of Pygame for interactive dashboards and customizable play. 
Historically, sugar operations included GTK as a key component. This is the official [documentation](https://www.gtk.org/docs/) for GTK,
where we can get all of the information we need.

The majority of Sugar developers are currently utilizing GTK3, an enhanced version of GTK, to construct activities. 
My task is to create a document with basic details on the most often used GTK methods in Sugar.

### Challenges I faced🙃
Finding a proper documentation which contains all the GTK commands or examples with code snippets was really a challenging tasks. Unlike the pygame document it was nowhere to be found. This motivated me to manually create one document containing all the details and meeting all our requirement.

### Solution👨‍💻
To solve this problem I started exploring the functionalities and all the methods mentioned on this website- https://devdocs.io/gtk~3.20/ 
This helped me understand and filter out all the important stuff from the website and store it in my manual.

### Dataset
These are the 2 datasets which I have prepared out of which following refernces I have listed below. I have scrapped as much as relevant data I could. Beecause of lack of expertise in GTK I am unable to filter out the irreleveant content of this. Once I get time I would get in touch with my mentors to clean these datasets so that it's free of irrelevant or less frequently used content.

Dataset 1:- Based on only [GTK-3.0](https://docs.google.com/document/d/1cNDJCE6fYY98mJfrjE5jxV4w7c8ycOBiuhszb3rIA-o)

Dataset 2:- Based on [Python GTK+3](https://docs.google.com/document/d/1FzCTppj3oaWzgMofojfJ8ZlhPPANuNKcZsdfk8SxtNc)

### Outputs

## Models I have tried🦙
In my previous blogs I had described the output of some Llama models which I had actually tried out of the entire Llama family. Best part about the code is that it works for all AI-models of the Llama-2 and Llama-3 family models available on huggingface. 

**Llama-2 Family**

![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Output/Models/Llama2%20fam.png)

**Llama-3 Family**
![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Output/Models/Llama3%20fam.png)

**These all models are available to us in different sizes, like 7B, 13B, 70B for Llama2 and 8B, 70B for Llama3. These denotes that how many billions of adjustable parameters does the model have.**

**Note:-** It's not possible for me to run the 70B models on google colab because they require a lot's of RAM storage to save the parameters. But yes all other LLMs can be made to run on the colab file.
## References
These are some resources for referrals offered by my mentor Ibiam. These were quite beneficial in the creation of the document.

https://python-gtk-3-tutorial.readthedocs.io/en/latest/

https://lazka.github.io/pgi-docs/

These links contained in-depth information about each GTK function it's use case with a small code snippet

https://devdocs.io/gtk~3.20/

https://docs.gtk.org/gtk3/index.html

# Summary
With this, I have successfully implemented the chatbot. This model can now do the following four functions as needed.
1. Generating Codes
2. Fixing code snippets
3. Navigating through pygame library
4. Traversing the basic GTK functions

A full-fledged AI-chatbot has been implemented with all it's core features we had discussed. However I had planned to take this thing to an entirely next level‼ 

# Plan for next week📝
Our Pippy AI-assistant will be incomplete unless it is able to provide some example programs from which Sugar activities may be created. These codes would serve as a reference and help sugar developers grasp the overall structure of Sugar's software. The next week, this would be part of my action plan. 

Aside from that, I want to reinstall the Sugar desktop environment on my virtual machine for development purposes(as it has some complications currently). This is because I have completed the AI part of the project and need to focus my attention on the UI of the Pippy activity, where the LLM will interact with the children.

This would allow for a basic figma-style drawing of how our UI will seem.
