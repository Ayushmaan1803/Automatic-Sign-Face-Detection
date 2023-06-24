
# Automatic-Sign-Face-Detection

The purpose of the project in this use case is threefold. First and foremost, it aims to address the issue of faulty admit cards that arises due to trainees mistakenly uploading their signatures instead of their photos. This problem negatively impacts the trainees, as it can lead to confusion and potential complications during the examination process. By developing a system that utilizes automatic analysis of uploaded documents, the project aims to rectify this error by identifying and correcting the misplaced documents. This would ensure that the correct photos are uploaded in place of the signatures, eliminating the occurrence of faulty admit cards.
It also seeks to support trainees from poor backgrounds who possess below-average computer skills. These individuals may face challenges in navigating the computer systems required for the examination process. By implementing an AI-based solution that automatically analyzes the uploaded documents, the system can alleviate the burden on trainees by seamlessly placing the correct documents at the right location on the portal. This approach would require minimal intervention from the trainees themselves, reducing the risk of errors and streamlining the process for those with limited computer proficiency.



## Installation

Step1: Clone the repository.
  ```
  $ git clone https://github.com/SHUDDHASHIL21/Automatic-Sign-Face-Detection.git
  ```
Step2: Open the main.py file in your local python IDE

Step3: Install all the dependencies from requirements.txt and run this in your terminal.
  ```
  $ pip install -r requirements.txt
  ```

Step4: Run the streamlit app.
  ```
   $ streamlit run main.py
  ```


## Usage

There are four use cases in checking the documents-


1)1st place is face image & 2nd place is signature image: 
In this case no swapping is needed as documents are uploaded at proper places.
 
2)1st place is signature image & 2nd place is face image: 
In this case swapping is needed and the program will automatically swap the images by detecting the images using the AI model.
	
3)Both are face images:
In this case the program will print ‘Both are face images , please upload correct documents!!!’ 
 
4)Both are signature images:
In this case the program will print ‘Both are signatures, please upload correct documents!!!’
 

## Authors

- [@rounakbhowmick123](https://github.com/rounakbhowmick123)

- [@SHUDDHASHIL21]( https://github.com/SHUDDHASHIL21)

- [@ Ayushmaan1803](https://github.com/Ayushmaan1803)

- [@sayantanmaji10](https://github.com/sayantanmaji10)




