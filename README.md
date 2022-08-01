# Introduction
Simple example script to bulk-delete Slack messages.
- Based on: https://github.com/sgratzl/slack_cleaner2
- Examples: https://github.com/sgratzl/slack-cleaner/issues/79

```bash
# Build the Docker image
docker build -t slack_cleaner .

# Run the script inside a container
cat script.py | docker run -i --rm -e SLACK_TOKEN=[token-here] slack_cleaner
```