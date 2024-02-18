# Spotify Button
Transform your physical button into a remote control for Spotify, enabling music management directly from your fingertips.

<img src="images/spotify-button-illustration.png" alt="Spotify Button Illustration" width="500"/>



## Features

- **Playlist Addition**: Press the button to add the currently playing Spotify track to a specified playlist.
- **Track Deletion**: In case of mistake, just double press to delete the last added track, provided it was within the last 10 minutes.
- **Audible Feedback**: Volume patterns indicate the success or failure of the action, providing immediate auditory feedback.


## Deployment

The endpoint is deployed on GCP Cloud functions.

## Getting Started

To get your Spotify Button up and running, follow these steps:

### Requirements

Ensure you have the following prerequisites installed:

- Python 3.x
- `spotipy` Python library (version 2.14.0 as specified in `requirements.txt`)

### Setup

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Install Dependencies**: Run `pip install -r requirements.txt` to install the necessary Python libraries.

3. **Environment Variables**: Set up the following environment variables:
   - `SPOTIFY_USERNAME`: Your Spotify username.
   - `SPOTIPY_CLIENT_ID`: Your Spotify API Client ID.
   - `SPOTIPY_CLIENT_SECRET`: Your Spotify API Client Secret.
   - `SPOTIPY_REFRESH_TOKEN`: Your Spotify API Refresh Token.
   - `SPOTIPY_REDIRECT_URI`: Your Spotify API Redirect URI.
   - `PLAYLIST_ID`: The Spotify Playlist ID where tracks will be added or removed.
   - `APP_SECRET`: A secret token for authenticating requests to your endpoint.

4. **Deployment**: Deploy your application to GCP Cloud Functions, ensuring all environment variables are correctly set in the cloud environment.

### Usage

- To **add** the current playing track to the specified playlist, send a request with the parameter `add` to your cloud function's endpoint.
- To **delete** the recently added track, send a request with the parameter `delete` within 10 minutes of adding the track.

Ensure to authenticate your requests using the `APP_SECRET` token.

### Example

```python
import requests

# Example of adding a track
requests.get('YOUR_CLOUD_FUNCTION_ENDPOINT?add=true&token=YOUR_APP_SECRET')

# Example of deleting a track
requests.get('YOUR_CLOUD_FUNCTION_ENDPOINT?delete=true&token=YOUR_APP_SECRET')
```

Replace `YOUR_CLOUD_FUNCTION_ENDPOINT` with your actual endpoint URL and `YOUR_APP_SECRET` with your `APP_SECRET` environment variable value.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
