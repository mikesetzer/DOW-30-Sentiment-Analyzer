# Michael Setzer, Megan Barrick, Lily Fernandez, Wisvrick Amisial
# PID: 3294008, 5521240, 4547426, 0374525
# Date: 10/30/22
# Python implementation for a sentiment analyzer

from textblob import TextBlob
import nltk
import pandas as pd
from nltk.tokenize import WordPunctTokenizer

# Imports to fix utf8 encoding issues
import sys
from importlib import reload
reload(sys)
sys.getdefaultencoding()


# Relative Proportional Sentiment Score formula: Formula: (P-N) / (P+N)
# Where P is the count of positive coded sentiments and
# Where N is the count of negative coded sentiments
def sentiment_score(p, n):
    if p == 0 and n == 0:
        print("Error: No positive or negative coded sentiments found.")
        quit()
    elif p == 0:
        print("No positive coded sentiments found.")
    elif n == 0:
        print("No negative coded sentiments found.")
    else:
        return (p - n) / (p + n)


# Prompt user for stock selection and analyze the selected stock
def sentiment_analysis():
    # Prompt user for selection
    print("\nWelcome to Group 3's Sentiment Analyzer for the DOW 30.\n")
    print("========================================")

    # Store set of user options as d for table display
    d = {
        1: ("AAPL", "AMGN", "AXP", "BA", "CAT"),
        2: ("CRM", "CSCO", "CVX", "DIS", "DOW"),
        3: ("GS", "HD", "HON", "IBM", "INTC"),
        4: ("JNJ", "JPM", "KO", "MCD", "MMM"),
        5: ("MRK", "MSFT", "NKE", "PG", "TRV"),
        6: ("UNH", "V", "VZ", "WBA", "WMT")
    }

    # Print dictionary as a table
    for k, v in d.items():
        c1, c2, c3, c4, c5 = v
        print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(c1, c2, c3, c4, c5))
    print("========================================\n")

    # Convert user selection to uppercase to catch case mismatches
    stock_sel = input("Enter a stock from the list above, or type exit or quit.\n").upper()

    # Verify user input and assign source file based on input
    print("You have selected", stock_sel)
    match stock_sel:
        case "AAPL":
            src_file = 'SentimentAnalyzer/Articles/AAPL/aapl.txt'
        case "AMGN":
            src_file = 'SentimentAnalyzer/Articles/AMGN/amgn.txt'
        case "AXP":
            src_file = 'SentimentAnalyzer/Articles/AXP/axp.txt'
        case "BA":
            src_file = 'SentimentAnalyzer/Articles/BA/ba.txt'
        case "CAT":
            src_file = 'SentimentAnalyzer/Articles/CAT/cat.txt'
        case "CRM":
            src_file = 'SentimentAnalyzer/Articles/CRM/crm.txt'
        case "CSCO":
            src_file = 'SentimentAnalyzer/Articles/CSCO/csco.txt'
        case "CVX":
            src_file = 'SentimentAnalyzer/Articles/CVX/cvx.txt'
        case "DIS":
            src_file = 'SentimentAnalyzer/Articles/DIS/dis.txt'
        case "DOW":
            src_file = 'SentimentAnalyzer/Articles/DOW/dow.txt'
        case "GS":
            src_file = 'SentimentAnalyzer/Articles/GS/gs.txt'
        case "HD":
            src_file = 'SentimentAnalyzer/Articles/HD/hd.txt'
        case "HON":
            src_file = 'SentimentAnalyzer/Articles/HON/hon.txt'
        case "IBM":
            src_file = 'SentimentAnalyzer/Articles/IBM/ibm.txt'
        case "INTC":
            src_file = 'SentimentAnalyzer/Articles/INTC/intc.txt'
        case "JNJ":
            src_file = 'SentimentAnalyzer/Articles/JNJ/jnj.txt'
        case "JPM":
            src_file = 'SentimentAnalyzer/Articles/JPM/jpm.txt'
        case "KO":
            src_file = 'SentimentAnalyzer/Articles/KO/ko.txt'
        case "MCD":
            src_file = 'SentimentAnalyzer/Articles/MCD/mcd.txt'
        case "MMM":
            src_file = 'SentimentAnalyzer/Articles/MMM/mmm.txt'
        case "MRK":
            src_file = 'SentimentAnalyzer/Articles/MRK/mrk.txt'
        case "MSFT":
            src_file = 'SentimentAnalyzer/Articles/MSFT/msft.txt'
        case "NKE":
            src_file = 'SentimentAnalyzer/Articles/NKE/nke.txt'
        case "PG":
            src_file = 'SentimentAnalyzer/Articles/PG/pg.txt'
        case "TRV":
            src_file = 'SentimentAnalyzer/Articles/TRV/trv.txt'
        case "UNH":
            src_file = 'SentimentAnalyzer/Articles/UNH/unh.txt'
        case "V":
            src_file = 'SentimentAnalyzer/Articles/V/v.txt'
        case "VZ":
            src_file = 'SentimentAnalyzer/Articles/VZ/vz.txt'
        case "WBA":
            src_file = 'SentimentAnalyzer/Articles/WBA/wba.txt'
        case "WMT":
            src_file = 'SentimentAnalyzer/Articles/WMT/wmt.txt'
        case "QUIT" | "EXIT" | "Q":
            print("Thank you for using Group 3's DOW 30 Sentiment Analysis tool.")
            exit(0)
        # Default case, if selection is invalid exit program after confirmation
        case _:
            print("Invalid stock was entered.")
            # Pause the terminal until user chooses to exit
            a = input('Enter any key to exit.\n')
            if a:
                exit(0)

    # Read selected source file to read var, force utf-8 encoding and ignore non utf-8 chars
    read = open(src_file, 'r', encoding="utf-8", errors="ignore").read()

    # Tokenize the words, convert article to uppercase to match csv, remove non UTF-8 junk
    article = WordPunctTokenizer().tokenize(read.upper())

    # Create panda list for positive and negative csvs
    positive_list = pd.read_csv('SentimentAnalyzer/LoughranMcDonald_Positive.csv', names=['positive_words'])
    negative_list = pd.read_csv('SentimentAnalyzer/LoughranMcDonald_Negative.csv', names=['negative_words'])

    # Convert panda objects to standard python lists
    positive_dict = positive_list['positive_words'].tolist()
    negative_dict = negative_list['negative_words'].tolist()

    # Create lists of positive and negative words in article using positive/negative_dict
    article_positives = [word for word in article if word in positive_dict]
    article_negatives = [word for word in article if word in negative_dict]

    # Print lists of positive/negative coded sentiments in documents
    print("\nPositive terms found:", article_positives)
    print("Negative terms found:", article_negatives)

    # Open classifier files and build dictionary
    positive_score = len(article_positives)
    negative_score = len(article_negatives)

    # Print count of positive and negative coded sentiments
    print("Positive score:", positive_score)
    print("Negative score:", negative_score)

    # Pause for input before closing
    print("Sentiment score for", stock_sel, "is", sentiment_score(positive_score, negative_score))

    # Pause the terminal until user chooses to exit
    a = input('\nEnter c to continue or press any key to exit.\n')
    if a == 'c':
        # Resume program
        sentiment_analysis()
    else:
        # End sentiment analysis tool
        print("Thank you for using Group 3's DOW 30 Sentiment Analysis tool.")
        exit(0)


# Initialize program
sentiment_analysis()
