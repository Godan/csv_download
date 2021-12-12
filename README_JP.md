# csv_download
csvでURLが記載された列を指定して一括でダウンロードして保存するスクリプト


## usage 

`csv_download`はcsvを読み込んで指定された列のURLを順々にダウンロードします。
使用できるオプションは`-h`で確認することができます
```shell
$ csv_download  -h

usage: csv_download [-h] [-o OUT_PATH] [-p PREFIX] [-t TARGET_URL_COLUM] [-n NAME_COLUM] [--sleep SLEEP] [--header-skip] file path

positional arguments:
  file path

optional arguments:
  -h, --help            show this help message and exit
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