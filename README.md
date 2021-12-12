# csv_download
Script to specify the column with URL in csv and download and save in bulk.


## usage

`csv_download` reads csv and downloads the URLs of the specified columns in sequence.
You can see the available options with `-h`
```shell
$ csv_download -h

usage: csv_download [-h] [-o OUT_PATH] [-p PREFIX] [-t TARGET_URL_COLUM] [-n NAME_COLUM] [--sleep SLEEP] [--header-skip] file path

positional arguments:
   file path

optional arguments:
   -h, --help show this help message and exit
   -o OUT_PATH, --out OUT_PATH
   -p PREFIX, --prefix PREFIX
   -t TARGET_URL_COLUM, --target-url-col TARGET_URL_COLUM
   -n NAME_COLUM, --name-col NAME_COLUM
   --sleep SLEEP
   --header-skip
```

### example
```shell
$ csv_download ./example/example.csv -o ./image -p example --header-skip
```

## Author
[Godan](https://github.com/godan)



Translated with Google Translate