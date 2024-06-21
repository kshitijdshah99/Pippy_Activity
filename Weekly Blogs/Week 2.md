# Outline
Last week as discussed I completed with the the python code generation part and the code correction part.
I tried looking at how good the models where at correcting kids code and the accuracy was quite profecient.

# Week 2

### 1. Code correction⚠
I started this week looking at proper datasets for code correction. 
These where some of the datasets which I had found online on kaggle and some other websites like hugging face. I dicussed these details with my mentor Walter and got an approval from him saying it works as long as things don't get complicated for kids.

https://www.kaggle.com/datasets/veeralakrishna/python-code-data

https://huggingface.co/datasets/jtatman/python-code-dataset-500k/viewer/default/train

https://huggingface.co/datasets/flytech/python-codes-25k

https://huggingface.co/datasets/luisroque/instruct-python-llama2-500k/viewer/default/train?row=73

I did try training the model on google colab on following datasets but I observed following issue. 
![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/GPU%20limit.png)

Colab offers 12 hours of GPU runtime and 15GB of free space. However this is not sufficient for training models on large datasets which I had shortlisted above so the idea of fine-tuning our shortlisted models like Llama2, Codellama and Llama3 was then discarded. 
