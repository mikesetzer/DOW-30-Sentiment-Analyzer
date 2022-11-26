# DOW-30-Sentiment-Analyzer

This is a sentiment analysis tool built for analyzing .txt converted journal articles regarding DOW 30 index stocks.

==========

### Required file structure:
```
project
│   README.md
│   sentiment_analyzer.py    
│
└───SentimentAnalyzer
│   │   LoughranMcDonald_Negative.csv
│   │   LoughranMcDonald_Positive.csv
│   │
│   └───Articles
│       └───AAPL
│           │    aapl.txt
│       │   ...
│       │   ...
│       │   ...
|       └───WMT
│           │    wmt.txt
```

==========

### Required packages (without using packaged file):
- pip install -U textblob
- pip install ntlk
- pip install pandas

==========

### Final sentiment score method: 
#### Relative Proportional Difference, Bounds [-1, 1]

Formula: (P-N) / (P+N)

Where P = count of positive coded sentiment words
	N = count of negative coded sentiment words

Score is not regarded, only count of words.

==========

#### Method source: https://rdrr.io/github/quanteda/quanteda.sentiment/f/vignettesSentiment_analysis.Rmd

==========

### Method breakdown:

- Request user choice, select a stock from the available list in the DOW 30
- Assign source files based on user selection
- Force utf-8 encoding on article text to remove any non alphanumeric characters
- Tokenize article text, removing punctuation & assigning words as list items
- Create lists of pos/neg coded sentiments from Loughran McDonald csvs
- Remove pos/neg words from article text and add to pos/neg lists
- Display lists of found coded sentiments
- Count sum of pos/neg terms in each list
- Display total pos/neg found coded sentiments
- Calculate sentiment score using Relative Proportional Sentiment Score formula
- Display sentiment score to user

==========

## Final sentiment scores:
- (Score)
	- (Positive coded sentiments)
	- (Negative coded sentiments)
	- (Relative Proportional Difference)

- AXP (American Express) 	
	- 64
	- 49
	- 0.13274336283185842
- AMGN (Amgen)			
	- 56
	- 138
	- -0.422680412371134
- AAPL (Apple)			
	- 72
	- 123
	- -0.26153846153846155
- BA (Boeing Co)			
	- 21
	- 85
	- -0.6037735849056604
- CAT (Caterpillar)		
	- 38
	- 33
	- 0.07042253521126761
- CSCO (Cisco Systems)		
	- 129
	- 77
	- 0.2524271844660194
- CVX (Chevron)			
	- 26
	- 75
	- -0.48514851485148514
- GS (Goldman Sachs Grp)	
	- 40
	- 121
	- -0.5031055900621118
- HD (Home Depot)			
	- 112
	- 223
	- -0.33134328358208953
- HON (Honeywell Intnl)		
	- 20
	- 123
	- -0.7202797202797203
- IBM (IBM Corp)			
	- 26
	- 24
	- 0.04
- INTC (Intel Corp)		
	- 24
	- 64
	- -0.45454545454545453
- JNJ (Johnson & Johnson)	
	- 13
	- 191
	- -0.8725490196078431
- KO (Coca-Cola Co)		
	- 56
	- 34
	- 0.24444444444444444
- JPM (JPMorgan Chase)		
	- 35
	- 230
	- -0.7358490566037735
- MCD (McDonald's Corp)		
	- 52
	- 89
	- -0.2624113475177305
- MMM (3M Co)			
	- 27
	- 127
	- -0.6493506493506493
- MRK (Merck & Co)			
	- 13
	- 7
	- 0.3
- MSFT (Microsoft Corp)		
	- 56
	- 105
	- -0.30434782608695654
- NKE (Nike Inc)			
	- 89
	- 132
	- -0.19457013574660634
- PG (Proctor & Gamble)		
	- 136
	- 78
	- 0.27102803738317754
- TRV (Travelers Co)		
	- 53
	- 168
	- -0.5203619909502263
- UNH (UnitedHealth Grp)	
	- 45
	- 61
	- -0.1509433962264151
- CRM (Salesforce)			
	- 77
	- 44
	- 0.2727272727272727
- VZ (Verizon Comm)		
	- 31
	- 85
	- -0.46551724137931033
- V (Visa)				
	- 37
	- 124
	- -0.5403726708074534
- WBA (Walgreens Boots)		
	- 81
	- 50
	- 0.2366412213740458
- WMT (Walmart)			
	- 66
	- 52
	- 0.11864406779661017
- DIS (Walt Disney Co)		
	- 244
	- 129
	- 0.30831099195710454
- DOW (DOW Inc)			
	- 160
	- 112
	- 0.17647058823529413
