# Last Collage - a playground with [Last.fm API](https://www.last.fm/api) and [Chalice](https://github.com/aws/chalice).

Last Collage allows you to create beautiful collages of your favorite artists based on your Last.fm history.

## Getting Started

Just remember your `<lastfm_user>` and put it in the end of the link.

```
https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/collage/<lastfm_user>
```

And you will get a JSON response with the link to a stunning collage like the one below.

<p align="center">
  <img src="https://s3.amazonaws.com/g4brielvs/9f7e2e5efcd94055a101b9610979c53e" width="400" height="400" />
</p>



## How do I get up and running?

You only need to set up your environment variables and install the packages in your virtualenv.

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

#### Status

##### `GET /api/`

#### Collage

##### `GET /api/<lastfm_user>/`

#### Upload

##### `POST /api/upload/`

## Examples

```
curl -X GET https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/"
```

```
curl -X GET https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/collage/g4brielvs"
```

```
curl -X POST https://ybnryhkb94.execute-api.us-east-1.amazonaws.com/api/upload --upload-file example.png --header "Content-Type:application/octet-stream"
```
