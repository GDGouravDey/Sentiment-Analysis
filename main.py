from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')

choice = '-1'

while(choice != '0'):
    choice = input("\nEnter 1 for Manual Input or 2 for URL Input, or 0 to Exit: ")
    if(choice=='0'):
        print("\nExiting Program...\n")
        break
    elif(choice=='1'):
        text = input("\nEnter Text: ")
    elif(choice=='2'):
        url = input("\nEnter URL: ")
        article = Article(url)

        try:
            article.download()
            article.parse()
            article.nlp()
        
        except Exception as e:
            print(f"\nError downloading/parsing article: {e}")
            continue

        ch = input("\nEnter 1 for Full Page Evaluation or 2 for Page Summary Evaluation: ")
        if(ch=='1'):
            text = article.text
        elif(ch=='2'):
            text = article.summary
        else:
            print("\nInvalid Input. Try Again.\n")
            break
    else:
        print("\nInvalid Input. Try Again.")
        continue
    print('\n'+text+'\n')

    blob =  TextBlob(text)
    sentiment = blob.sentiment.polarity
    print("Sentiment Value ( -1 to 1 ) = ",sentiment,'\n')

    if(sentiment<0.1 and sentiment>-0.1):
        print("Sentiment is Neutral.")
    elif(sentiment>=0.1 and sentiment<0.3):
        print("Sentiment is Somewhat Positive.")
    elif(sentiment>=0.3 and sentiment<0.6):
        print("Sentiment is Positive.")
    elif(sentiment>=0.6):
        print("Sentiment is Extremely Positive.")
    elif(sentiment<=-0.1 and sentiment>-0.3):
        print("Sentiment is Somewhat Negative.")
    elif(sentiment<=-0.3 and sentiment>-0.6):
        print("Sentiment is Negative.")
    elif(sentiment<=-0.6):
        print("Sentiment is Extremely Negative.")