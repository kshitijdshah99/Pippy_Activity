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

### Lack of proper datasets
Pygame is a python library however it's dataset is not generic as python code datasets are. I tried googling and searching on kaggle, hugggingface but could not find even a trace of it. I communicated this problem to my mentor Ibiam in a meet, he suggested me to manually create one dataset for the same. He provided me some repository links of sugar activities and advised me to scrap out content from it.

These are some of those repos:-

Sugargame test activity - https://github.com/sugarlabs/sugargame/tree/master/test

Pippy - https://github.com/sugarlabs/Pippy

StickHero - https://github.com/sugarlabs/stick-hero-activity

Across and Down - https://github.com/sugarlabs/across-and-down-activity

TicTacToe - https://github.com/sugarlabs/tictactoe

Math Hurdler - https://github.com/sugarlabs/math-hurdler

Hit the balls - https://github.com/sugarlabs/hittheballs-activity

Fifty two activity - https://github.com/sugarlabs/fifty-two-activity

I tried doing the same however the accuracy was not upto the mark and the results generated were quite random

### Shortage of GPU resources for fine-tuning
Making situation worse the lack of compute resources made it more difficult to train on the manually created datasets. It was observed that as soon as the GPU usage of 15GB was exhausted the fine-tuning was stopped. For fine-tuning the models are trained on a dataset for 50-100 or even more epochs. More epochs means more GPU run time and also more usage. This was most difficult problem to be solved.

### Low accuracy
One common doubt which may arise is that pygame being a python library can be well understood by models like codellama then what's the issue with that.
1. Cannot generate complex codes
2. Codes it generated had several syntax and logical errors

These all errors made me think of an entirely different approach RAG for acheiving our tasks.


