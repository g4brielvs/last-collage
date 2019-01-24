# Last Collage - a playground with [Last.fm API](https://www.last.fm/api) and [Chalice](https://github.com/aws/chalice).

Last Collage allows you to create beautiful collages of your favorites artirst based on your Last.fm history.

Just remember your `<lastfm_user>` and follow the link.

[https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/collage/<lastfm_user>](https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/collage/)

And you will receive a link to a stunning collage like the one below.

<img src="https://s3.amazonaws.com/g4brielvs/9f7e2e5efcd94055a101b9610979c53e" width="400" height="400" />

## How do I get up and running?

You only need to set up your environment variables and install the packages in your virtualenv. And hit ```

```
pip install -r requirements.txt
```

And hit RUN!

```
chalice local
```

### Environment settings

* `AWS_ACCESS_KEY_ID` (_str_) 
* `AWS_SECRET_ACCESS_KEY` (_str_) 
* `BUCKET` (_str_) 
* `LAST_FM_API` (_str_)

### JSON API endpoints

#### Collage

##### `GET /api/<lastfm_user>/`

#### Status

##### `GET /api/status/`

#### Upload

##### `POST /api/upload/`

## Examples

```
curl -X GET https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/collage/g4brielvs"
```

```
curl -X GET https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/status"
```

```
curl -X POST https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/upload --upload-file example.png --header "Content-Type:application/octet-stream"
```
