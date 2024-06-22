# Progress till now📈
Last week as discussed I completed with the the python code generation part and the code correction part.
I tried looking at how good the models where at correcting kids code and the accuracy was quite profecient.

# Week 2

## 1. Code correction⚠
I started this week looking at proper datasets for code correction. 
These where some of the datasets which I had found online on kaggle and some other websites like hugging face. I dicussed these details with my mentor Walter and got an approval from him saying it works as long as things don't get complicated for kids.

https://www.kaggle.com/datasets/veeralakrishna/python-code-data

https://huggingface.co/datasets/jtatman/python-code-dataset-500k/viewer/default/train

https://huggingface.co/datasets/flytech/python-codes-25k

https://huggingface.co/datasets/luisroque/instruct-python-llama2-500k/viewer/default/train?row=73

I did try training the model on google colab on following datasets but I observed following issue. 
![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/GPU%20limit.png)

Colab offers 12 hours of GPU runtime and 15GB of free space. However this is not sufficient for training models on large datasets which I had shortlisted above so the idea of fine-tuning our shortlisted models like Llama2, Codellama and Llama3 was then discarded. 

**Yes, I could not fine-tune the models due to unavailability of GPUs, however the models still where too good in correcting codes of the kids this is because they contained very easy syntax or logical errors. Too easy to be understood by our LLMs😅. This motivated me to focus on our next feature of AI-asisstant i.e. Pygame basics.**


## 2. Pygame Basics🐍
Codebase of Sugar activities is entirely formed of the Pygame and GTK libraries. Hence it is unavoidable to make our co-plot model devoid of these necessary features, else it would be incomplete. 
While trying to ingrate this feature I faced following issues with it.

a. Lack of proper datasets
b. Shortage of GPU resources for fine-tuning
c. Low accuracy

### a. Lack of proper datasets
Pygame is a python library however it's dataset is not generic as python code datasets are. I tried googling and searching on kaggle, hugggingface but could not find even a trace of it.
#### Solution we tried
I communicated this problem to my mentor Ibiam in a meet, he suggested me to manually create one dataset for the same. He provided me some repository links of sugar activities and advised me to scrap out content from it.

These are some of those repos:-

Sugargame test activity - https://github.com/sugarlabs/sugargame/tree/master/test

Pippy - https://github.com/sugarlabs/Pippy

StickHero - https://github.com/sugarlabs/stick-hero-activity

Across and Down - https://github.com/sugarlabs/across-and-down-activity

TicTacToe - https://github.com/sugarlabs/tictactoe

Math Hurdler - https://github.com/sugarlabs/math-hurdler

Hit the balls - https://github.com/sugarlabs/hittheballs-activity

Fifty two activity - https://github.com/sugarlabs/fifty-two-activity

#### Results
I tried doing the same however the accuracy was not upto the mark and the results generated were quite random

### b. Shortage of GPU resources for fine-tuning
Making matters worse, a shortage of computational resources makes it more difficult to train on manually prepared datasets. It was discovered that fine-tuning ended as soon as the GPU's 15GB utilization was exhausted. For fine-tuning, the models are trained on a dataset for 50-100 or more epochs. higher epochs result in higher GPU run time and utilization. This was the most hardest challenge to tackle.

#### Solutions We Tried
Our mentors Walter, Ibiam, and Devin began emailing cloud computing businesses about funding and supporting us with a few compute units. 

#### Results:
We were unable to secure a subscription from the firms we emailed, therefore the problem of a lack of resources continued.

### c. Low accuracy.
One recurrent question is whether pygame, as a Python library, can be easily understood by models such as codellama.
1. Cannot produce complicated codes.
2. The codes it created included various syntax and logical mistakes.

All of these obstacles prompted me to consider a completely new strategy to completing our objectives. RAG requires fewer resources while producing the expected results. Hence we diverted our focus to RAG approach. 

## 3. Sugar Presentation🖥
This week our mentors had scheduled a Live youtube streaming video in which we all had to present our ideas and our workflow for the project we where working on.

Click [here](https://www.youtube.com/live/k7eY-tkl2zw?si=uYhDzTmQB50bgJ48) to view all the Sugar Projects for GSoC'24 and DMP program.

This is the link to my PPT which I presented- [PPT](https://docs.google.com/presentation/d/11dck4oTrR32J-sOLBcb10KWExGrtwmlM/edit?usp=drive_link&ouid=105835308257191314131&rtpof=true&sd=true)




