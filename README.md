# Introduction
Topic modelling can be used to classify a text documents into their corresponding topics. There are algorithms that can find the distributions of certain keywords and their combinations within the documents. Then high density collections of keywords can be called a topic. Here is a descriptive image for such models. The larger the words represent the higher frequency within the corresponding topic. 
<IMG src="https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2018/05/22/sagemaker-ntm-6.gif"/>

Such topic modelling can be done on the collected user inquiries within the call centres or other communication channels within the organizations. These communication channels are phone calls, chatbots, digital avatars, surveys and etc. The first step in dealing with all these sources of conversatinos is to convert them to text and then apply NLP algorithms on them.  

# What are the topic models
The models are the collections of topics that exist in a text dataset. There are multiple levels of topic modelling based on the resolution of the topics. For example consider the articles in a newspaper, as the text data set that we want to apply modelling on it. By applying topic modelling we might end up with multiple topics collections (models). Here we call the models as model1, model2 and model3 with their topics among them. 
- Model 1 (topics)
1. Politics
2. Sports
3. Economy
4. Society
5. Other
- Model 2 (topics)
1. Foreign politics
2. National politics
3. Basketball
4. Rugby
5. Cricket
6. Other sports
7. Entertainment 
8. Life style
9. Business 
- Model 3 (topics)
1. Auckland news
2. Wellington news
3. Other NZ region news
5. World news
4. NZ sports
5. world sports
6. Technology
7. Travel
8. Life style 

As can be seen these models introduce different topics classification among the same document sets. All of them are valid and can be used based on the context. To pick the best model, we can check the keywords that each topic contains to see which ones is more relevant to the context. 

# Text topics modelling
One of the important uses of NLP is to analyze a text and find out its topic. Such analysis can be performed on a large train dataset and blindly find the topics within those texts. The created model can then be used to find the topic of any other texts within that dataset. To perform the modelling, some preprocessing should be done on the train dataset to clean it. The cleaned dataset will then be broken down to its forming words to create a bag-of-words representation of that text. A model will then be trained on the distribution of the collection of these bag-of-words. Such a model, can find the highest probable occurrences of the word combinations (their distribution) and then cluster them into topics. So each model can represent a collection of high probable for that specific topic which can be used for the classification of any new document. 

## Text cleanup
Within a text there are many grammar or language related words, acronyms, terms, phrases, etc. that do not contribute to the general topic of the text. Within the cleanup process, they can be removed from the text to have less and more descriptive words within the document. Some of these removed parts are emails, dates, acronyms, numbers, punctuations and stop words. 

## Tokenize words
In this step all each document is broken down into a list of words (tokens). After applying this step, each document containing many paragraphs and sentences can be represented with a list of important words within it. 

## Stemming and Lemmatization
Stemming is the process of converting the words of a sentence to its non-changing portions. Lemmatization is the process of converting the words of a sentence to its dictionary form. Here are some examples of applying these two algorithms in a document:
- am, are, is $\Rightarrow$ be 
- car, cars, car's, cars' $\Rightarrow$ car
- the boy's cars are different colors $\Rightarrow$ the boy car be differ color
After applying this step, all the variations of a word can be replaced with a single basic form of that word that can result in less number of representative words for each document. 

## Creating Lexicon and Corpus 
The corpus is the collection of words specific to a particular subject and lexicon is the vocabulary of a context that can be referred to as a dictionary. Using some proposed methods in NLP these entities can be created for the lists of words of the documents. 

## Building the topic model
One of the best topic modelling methods in NLP is Latent Dirichlet Allocation (LDA). LDA is used to classify text in a document to a particular topic. It builds a topic per document model and words per topic model, modeled as Dirichlet distributions. Each document is modeled as a multinomial distribution of topics and each topic is modeled as a multinomial distribution of words. LDA assumes that the every chunk of text we feed into it will contain words that are somehow related. Therefore choosing the right corpus of data is crucial. It also assumes documents are produced from a mixture of topics. Those topics then generate words based on their probability distribution.

The number of topics should be given to LDA algorithm and it will then generate the model. It is important to find the best number of topics that can represent the collection of documents. There are some measures that can show how good a model can find the number of topics, which is called coherence score. A good number of topics is a number that has least overlapping between the topics and each topic can cover big set of documents within the collection, and this can be represented by higher values of coherence score. To find this number, the model will be run to create models for a number of topics for example from 2 to 30 and then the coherence score will be measured for each model. The one that has the highest coherence score, will then be considered as the final model. 

An example of such modelling method was implemented using the Addons notes with types CAL and CNV collected in August 2018. The modelling process was repeated for the number of topics from 2 to 21 and coherence measure was calculated on them to find the best number of topics for the train document. The optimum number of topics in the model is 7 and the next best number of topics is 17 as shown in the following image. 


For the models with 7 and 17 topics the distribution of words can be seen in the attached models. These distributions show the high frequency key words in a descending order for each topic and are quite illustrative of the topics and their meaning. As an example the words distribution for the 7 topics in the model are as below:
![1.PNG](/.attachments/1-3b7eca91-0bf0-4a69-9381-4fa2596b0011.PNG)

![2.PNG](/.attachments/2-91953350-0add-4cb0-ab61-00c4c95009fe.PNG)

![3.PNG](/.attachments/3-3a1d1925-a393-43a1-8167-5dba77f71944.PNG)

![4.PNG](/.attachments/4-3faaa48c-9137-463e-a5bd-6a40b27303ed.PNG)

![5.PNG](/.attachments/5-c2934a8c-d83b-43a8-9b97-e8c5f043c5e6.PNG)

![6.PNG](/.attachments/6-80f35894-d69b-4777-ade9-e232de34acf4.PNG)

![7.PNG](/.attachments/7-e9c26b5e-cd11-45ef-b7a2-3cc78424b200.PNG)

By looking at the most frequent words of each topic we can have an idea of that topic and hence the notes that fall under that topic.  

## Applying the model
After creating the model, it can then be applied to all the new text entries in the system to classify them to the right topic. If the model illustrated in previous section is applied to a set of new documents, the returned value will then be a number from 1 to 7 for each document stating the topic of that document.

# Application of text topic models
Such modelling method was discussed in the previous section. These models can give us some understanding of the possible topics of any targeted communication channels. Knowing the topics of any document can give us the opportunity of analyzing and taking actions on it automatically. Some possible use cases of such modelling are discussed in this section. 








# What is a good model
There definitely are some overlap between the topics of a model. The best models are the ones that have very little overlap between their topics and cover almost all the regions (keywords distribution) of the text. In the following graphs, each graph represents a model and each circle represents a topic within that model. The plane of each graph represents the whole text dataset. The larger the circle, the larger that topic (covering more text and documents). The overlapping circles represent the common keywords among those topics. In these shown models, the first one represents a better model than the second one

![notes_1.PNG](/.attachments/notes_1-c833b5b0-eda5-4c58-a3b7-7c094e0aed33.PNG)

![notes_2.PNG](/.attachments/notes_2-39edb6d0-bbf7-498c-99a5-c8c30db96d80.PNG)

# How to create a topic model
One of the best algorithms to achive topic modelling is Latent Dirichlet allocation (LDA). In this method, every document in the text dataset is broken down to its forming words. These words are then tokenized and lemmatized

# How to measure how good a model is
In the execution of the modelling algorithm we can calculate a criterion called coherence value and shows how good the model topics classify the whole training set. The models (topics collections) with higher coherence values can be considered as good models. The modelling algorithm was applied on Addons notes for the number of topics varying from 2 to 41 and for each model the coherence value is calculated and shown in the following graph .
![coherence_values.png](/.attachments/coherence_values-012dd21b-a51f-4de9-b770-5b649f04a42b.png)
It can be seen that the model with 10 topics is the best (global maximum) model for the classification of the Addons notes. Each peak in the graph (local maximums) can also represent a relatively good model that can project different topics within the text. To make use of all the possible topics, 5 best models (peaks pf coherence values) are selected. In the descending order of the coherence value, models with 10, 13, 8, 20, 28 topics are selected. These models will look like the following graphs:
![model_10.PNG](/.attachments/model_10-4fb1f13d-a3bc-4a7d-8bc9-041313504a08.PNG)

![model_13.PNG](/.attachments/model_13-bb26c437-9eda-4055-9dc1-8d67b8214a33.PNG)

![model_8.PNG](/.attachments/model_8-eb27098c-688a-4743-b142-1bc07a2d1318.PNG)

![model_20.PNG](/.attachments/model_20-44117b5a-54d0-4f9d-8af5-d9c80a2c8c2b.PNG)

![model_28.PNG](/.attachments/model_28-45ed403c-b319-4b92-a83e-fda501a5a042.PNG)
In these graphs, each circle represents a topic. The sizes of circles are to represent the size of each topic, versus other ones. The overlapping circles show that there are common keywords between the corresponding topics. 


# How to use topic models
Such models can be used in the classification of any free text document. Such modelling method is applied to the Addons notes to classify them into classes. By looking at the keywords of each topic we can see that some of them contain word "ACC", and the docs under this topic can be related to Member Advocacy team. A time-consuming part of their job is to look for the ACC related notes and the proper ones. This text classification model can help them to spend less time on finding the ACC related notes. For example for the mentioned best model (the model with 10 topics), we can look at the keywords of each topic and see which ones have the word "ACC" in them. Then apply the model to any text within the dataset and see which texts fall under the topics with keyword "ACC" and then take them as ACC related texts. It can be seen that topics 2, 7, 9 and 10 contain the "ACC" keyword. 

![model_10_topic_2.PNG](/.attachments/model_10_topic_2-48bbbd1e-f1b7-492d-b5a2-e8f5780feb36.PNG)

![model_10_topic_7.PNG](/.attachments/model_10_topic_7-237b0d41-80db-47d8-aaa0-1b2d21ab7c1b.PNG)

![model_10_topic_9.PNG](/.attachments/model_10_topic_9-a77598d4-9c5b-408c-934e-a19505cda1f4.PNG)

![model_10_topic_10.PNG](/.attachments/model_10_topic_10-4a2e11b5-8525-4458-9e61-0bec9fa00656.PNG)

It can be seen that 4 topics of the total 10 topics have word ACC in them and the number of ACC keyword in topics 2, 7, and 10 are respectively high. These topics can be called "ACC related" in the model.

We can also look at the model with 28 topics since it covers more smaller topics. The topics with keyword ACC are as below:

![model_28_topic_5.PNG](/.attachments/model_28_topic_5-a536f366-05b8-44c5-b864-f7051fec68a1.PNG)

![model_28_topic_20.PNG](/.attachments/model_28_topic_20-77b3d22e-edc4-4f25-9642-237b1d3ead63.PNG)

![model_28_topic_25.PNG](/.attachments/model_28_topic_25-4cc40f00-3010-4426-bc57-437d9df53940.PNG)

![model_28_topic_27.PNG](/.attachments/model_28_topic_27-3a4ef43e-2855-4804-97d2-1c85bc99355f.PNG)

It can be seen that topics 25 and 27 have larger number of ACC keyword in them than the other two topics. For this model, these topics can be called "ACC related".

After finding the meaning of each topic in the model (by analyzing the keywords of that topic), we can then apply the model to any text to find its matching topic from the model. In this way, the model will give a weighting of the topics (summing to 1) for any new text. For example for the model with 10 topics, for an input text it might generated these numbers: topic1: 0.05, topic2: 0.1, topic3: 0.05, topic4: 0.5, topic5: 0.15, topic6: 0.02, topic7: 0.08, topic8: 0.01, topic9: 0.01, topic10: 0.03. By looking at the generated weightings, we can definitely say that the text falls under topic 4, since it has the biggest weight. 

# How to train model
There are multiple channels throughout the organization that are actively receiving the inputs from the customers, such as call center, chatbot, Addons, etc. which deal with customers and also internal transactions (Addons notes) between multiple teams. The generated text from all these channels can be used for training such models. For this purpose, call center is potentially the best channel at the moment since it is receiving numerous calls on a daily basis which are related plans, claim, prior approvals, user inquiries and etc. and since these calls are format free, training a model on them can become really representative of the data within other channels. 

# How to get the train set
We are using Bright Pattern platform for call center management and one of the key features of this platform is call recordings. We have huge set of audio recordings from the calls routed to the call center and using some speech to text services (on Azure) we can extract their corresponding texts to be used for model training purpose. 

# What are the benefits of such models
Since we aim to have very interactive communication channels with our customers, through chatbot and digital human, such model can give us an idea of the conversation context. Currently we have a limited knowledge-base for FAQs, but we can have more context specific knowledge bases that can cover the member concerns more accurately. If we can understand the context of the conversation using the model, then the conversation bot can use the context specific knowledge base or even take automated actions through the corresponding APIs throughout the organization. Such model can provide a means of integrating the chatbot or digital human with other platforms in the organization. 

Another use of the model is to find out how good the knowledge-bases cover the member concerns. We mentioned earlier that the model generates scores for how close the text is to each topic and then the topic with the highest score is considered as the topic of the input text. For example for a model with 4 topics, for an input text, if we get topic1: 0.8, topic2: 0.1, topic3: 0.05, topic4: 0.05, we can say that the input text definitely belongs to topic one with very high accuracy. But if we get topic1: 0.2, topic2: 0.2, topic3: 0.35, topic4: 0.25, we can consider the text as topic 3 but yet if has respectively high scores for other topics. This case is an indicator of a possibly new topic within the conversations that are not properly covered within the knowledge-base. This text can be reviewed and proper QnA pair can be added to the knowledge base to cover it. The we can have a new model with 5 topics that their weightings for this text entry may become topic1: 0.05, topic2: 0.01, topic3: 0.03, topic4: 0.01, topic5: 0.9. In this way we can have a dynamic knowledge-base that can change based on the member requirements. 

# How to achieve
| No. | Required actions | Status | Notes |
|--|--|--|--|
| 1 | Develop training algorithm in Azure | Done | The algorithm is developed in Python on Azure Databricks |
| 2 | Train a model as POC | Done | Trained on the call center Addons notes for 2018 (more than 4 million records). These records are extracted as CSV files and fed to the training algorithm |
| 3 | Test the model as POC | Done | Applied to the call center Addons notes for 2019 |
| 4 | Develop a dashboard as POC | Done | A Power BI dashboard is developed to show the topics of any call center text |
| 5 | Develop Speech to text platform | Done | Developed using Azure Cognitive services |
| 6 | Access Bright Pattern S3 bucket to get the audio files |  | The S3 bucket belongs to Southern Cross. This access needs some rights elevation |
| 7 | Develop an platform that can separate the member and agent conversations from the audio recordings |  |  |
| 8 | Apply the speech to text on the recordings and store the conversations text in an Azure database |  | Needs security approval to store this data on Azure since it might contain some sensitive data |
| 9 | Train the model on the member inquiries |  | Such model can be stored on Azure Blob storage since it contains no sensitive data |
| 10 | Analyze the model to verify the topics in Southern Cross context |  |  |
| 11 | Apply the model on the existing test dataset of member conversations |  | To verify the efficiency of the model |
| 12 | Develop an App service on Azure that can automatically collect the newly generated audio files from S3, convert them to text, store them in the DB, apply the model on them, publish the results to the DB |  |  |
| 13 | Design a dashboard specific to the teams that require the outcomes of such modelling procedure |  | For example some customized dashboard for customer experience team, claims team, etc. |

# What are the risks
We are dealing with real member conversations and hence it might contain some sensitive data. Since all these conversations are converted to text through Azure cognitive services, detecting the sensitive data in the text and removing them is really hard. It is possible to increase the security of Azure environment since it is controlled by us. If we can trust the Azure environment, then there are no other risks. 

# What is required 
Most of the development can be done within Data and Analytics team. There are two external requirements:
- Grant access to the Bright Pattern S3 bucket, which belongs to Southern Cross
- Final decision about where to store the converted member conversations, preferably on Azure SQL server. Implementation of security layers on the finalized storage. 

