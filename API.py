import twint

# Configure
c = twint.Config()
c.Search = "ヤサイ"
c.Output = "tweets.csv"
c.Store_csv = True
c.Since = "2021-06-01"
c.Until = "2021-07-01"

# Run
twint.run.Search(c)