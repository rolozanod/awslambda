import boto3

comprehend = boto3.client(service_name="comprehend")

text = "This is a bad day for the NBA"

payload = comprehend.detect_sentiment(Text=text, LanguageCode="en")

print(payload)