## Comprehend

- natural language processing service
- input = document
- output = entities, key phrases, language, sentiment, PII ...
- pre-trained models or custom
- `real-time` analysis for small workloads
- `async` jobs for larger workloads

## Forecast

- forecasting for time-series data
- import historical and related data
- output = forecast and forecast expandability

## Fraud Detector

- fully managed fraud detection service
- upload historical data and choose model type
- model type
  - `online fraud` : little historical data
  - `transaction fraud` : suspect payments
  - `account takeover` : phishing or other social based attack

## Kendra

- `intelligent search service`
- supports wide range of question types
- types of questions
  - `factoid` : who, what, where
  - `descriptive`: how
  - `keyword`
- `index` : searchable data organized in an efficient way
- `data source` : where data lives
  - kendra connects and indexes from this location
  - synchronize with index on a schedule
- documents : `structured or unstructured`

## Lex

- `text or voice conversational interfaces`
- automatic `speech recognition` (ASR)
- natural `language understanding` (NLU)
- `bots`
  - converse in 1+ languages
  - utterances : different ways something can be said
  - how to fulfil intent
    - usually lambda function
- slots
  - parameters for intent

## Polly

- turns text into lifelike speech
- tts types
  - standard tts
  - neural tts (much better)
- output formats : mp3, ogg vorbis ...
- Speech Synthesis Markup Language (SSML)
  - addition control on how polly generates speech
  - emphasis, pronunciation, whispering ...

## Rekognition

- deep learning based image and video analysis
  - identify object, people, content moderation ...
- pay per image

## SageMaker 

- fully managed machine learning service
  - fetch, clean, prepare, train, evaluate, deploy, monitor
- sagemaker studio : IDE for ML lifecycle
- sagemaker domain : isolation/grouping for a project
- containers : docker containers deployed to ml ec2 instance
- hosting : deploy endpoints for your models
- no cost : but the resources it creates do

## Textract

- detect and analyze text  contained in input documents
- input = JPEG, PNG, PDF, TIFF
- synchronous and asynchronous
- pay for usage
- detection of text
  - relationships in text, metadata
  - extracts fields from documents, receipts, IDs

## Transcribe

- automatic speech recognition (ASR)
- input = audio
- output = text
- pay as you use
- options
  - language customizable, filers for privacy, audience appropriate language, speaker identifier, custom vocabulary
- use case
  - index audio to allow searching
  - meeting notes
  - subtitles/captions and transcripts
  - call analytics

## Translate

- text translation service
  - translates text from one language to another
- ensures meaning is translated
- autodetect source text language
- use case
  - multi-language user experience

