# Spotify Button
Connects to a physical button to execute actions with Spotify.

- When the button is pressed, adds the music currently playing on Spotify to a playlist specified by the user.
- Double press: Delete the last music added (if added less than 10 min ago)
- Can _hear_ the result of the action: the volume of the music currently playing will decrease with a specific pattern if the action was successful, and with another pattern if it failed.

The endpoint is deployed on GCP Cloud functions.
