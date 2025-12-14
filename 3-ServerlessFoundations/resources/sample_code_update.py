def lambda_handler(event, context):

    # Extract values from the event
    emoji_type = event["emoji_type"]
    message = event["message"]

    # Log values
    print(emoji_type)
    print(message)

    # Initialize feeling variable
    feeling = None

    # Determine feeling based on emoji_type
    if emoji_type == 0:
        feeling = "positive"
    elif emoji_type == 1:
        feeling = "neutral"
    else:
        feeling = "negative"

    # Create response
    response = {
        "feeling": feeling,
        "message": message
    }

    return response
