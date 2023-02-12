# League Assessment

## Overview of stack:

Technologies leveraged: 
`Docker`
`Flask`
`Python3`

## Layers in application:

**`backend`**

The `api` folder is the main `Flask` application that leverges the entire backend, which accepts the CURL req for the File upload.

## Running environment

- `backend` - Port 5000

1. Clone repo
2. `cd` into repo folder, where `docker-compose.yml` lives
3. run `docker-compose up` and wait for all docker builds to run and all services to start and Python project to build
4. Verify Flask API service is running by seeing activity in termial or navigating to `localhost:5000` to  view back end health check

## CURL Commands for getting response for file upload

Make sure you are in the `dir` with the `docker-compose.yml` file and run following `cmd`:

`curl -F file=@files/matrix.csv http://localhost:5000/echo`

This will send the file `matrix.csv` that was sent with assessement email to correct endpoint

Output/Response should be:

```{
  "Flattened string": "1,2,3,4,5,6,7,8,9",
  "Inverted matrix formatted string": "1,4,7\n,2,5,8\n,3,6,9\n",
  "Matrix formatted string": "1,2,3\n,4,5,6\n,7,8,9\n",
  "Product of list": 362880,
  "Sum of integers": 45
}
```
Which should satify all requirements requested in the assessement `README.md`
