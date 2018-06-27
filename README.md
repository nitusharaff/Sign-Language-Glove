# Sign-Language-Glove


To bridge the communication gap between normal and speech impaired, we introduce a glove for hearing/speech impaired to facilitate the communication. The entire setup of our system consists of a glove to convert the hand gestures to speech and a User Interface which takes the input as speech and converts it to text and sign language gestures. Hence, an ease in conversation among the two parties.


![Alt text](/screenshot/glove.png)

The glove consists of various flex sensors to measure the bend of fingers and palm. It also consists of an accelerometer to measure the acceleration produced by some alphabets or words. Certain Machine Learning classification algorithms, like SVM, Random Forest, Decision Trees, Naïve Bayes and Neural Net, are employed to train the glove using the sensor values in order to match the correct speech format. The developed models are used in real time prediction of the sign language gestures to the speech and vice-versa. This overall process helps in a smooth communication between the two parties.






<h3>WEBSITE APPLICATION</h3>

The website application provides the user with an interface to interact with the device. The basic interface first allows the user to choose between two modules of conversion of sign language to audio or audio to video signs.

![Alt text](/screenshot/site.png)


The figure above shows the main page of the website when the user opens the link. He gets two options when he enters the page.

1) They can click on the recording button and speak to get the voice recorded. The submit button below it redirects to a new page with text converted into sign language videos.

2)The second option that the user has can do is to click for using the glove on the start button. The glove will then start taking in data in real time and redirect to a page showing the demonstrated sign language in the form of text and audio when the signs are over.



<h3>WORKING OF THE GLOVE </h3>

<strong> 1) DATA COLLECTION </strong>
In order to collect the sensors data and build a database, we use PLX-DAQ software. Data was collected demonstrating all alphabets and most frequently used set of words. The entire dataset has around 13000 values which are then being trained.

<strong> 1) DATA MODELING : MACHINE LEARNING </strong>
After obtaining the dataset, we train the model for type of alphabets and words in ASL using different algorithms. In order to evaluate and compare the performance, we choose four different classifiers for the learning process. We have also chosen the Python Scikit-learn platform to perform all the Machine Leraning modeling for our system.
The classifiers used were: 1. Support Vector Machines 2. Decision Trees 3. Random Forest 4.Naive Bayes 5. Multilayer Perceptron

Accuracy of the classifiers are shown below:</br>


![Alt text](/screenshot/accuracy.png)



<h3>AUDIO TO SIGN LANGUAGE </h3>

When the user speaks after clicking the record button in the website, a speech-to-text API is called and the text appears on the text box. These values are then sent for conversion into sign languages.The speech input recognized as text is mapped to audio files from the database and then displayed. 

![Alt text](/screenshot/gifs.png)


It must be noted that not all values of English language have a sign corresponding to it as per the American Sign Language Standard. That is, when people communicate through sign language, they do not need to frame entire sentences with correct English Grammar.


FILES:

Static: videos used in the database </br>
Templates: html websites templates</br>
arduino - codes for hardware</br>
connectdb.py- connect database</br>
dbconn.py- connect tables</br>
main.py - creates main page of website</br>
modeling.py- machine learning algorithms</br>
neuralnetwork.py - modeling neural nets</br>
requirements- list of hardware software used</br>
table insert.py - insertion to database tables</br>




