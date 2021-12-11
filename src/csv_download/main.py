import os
from optparse import OptionParser
import urllib.error
import urllib.request
import csv
import mimetypes
import time


def download_file(url, dst_path):
    with urllib.request.urlopen(url) as web_file:
        data = web_file.read()
        extension = mimetypes.guess_extension(web_file.headers["Content-Type"])
        with open(f"{dst_path}{extension}", mode="wb") as local_file:
            local_file.write(data)


def main(
    file_path: str,
    out_path: str,
    name_colum: int = 0,
    target_url_colum: int = 1,
    sleep_time: int = 1,
    prefix: str = "",
    header_skip: bool = False,
):
    csv_file = open(file_path, "r", errors="", newline="")
    list = csv.reader(
        csv_file,
        delimiter=",",
        doublequote=True,
        lineterminator="\r\n",
        quotechar='"',
        skipinitialspace=True,
    )
    if header_skip:
        next(list)
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    for row in list:
        try:
            download_file(
                row[target_url_colum], f"{out_path}/{prefix}{row[name_colum]}"
            )
            time.sleep(sleep_time)
        except ValueError:
            print(f"Can not download url:{row[name_colum]} / {row[target_url_colum]}")
        except urllib.error.URLError as e:
            raise Exception(f"Can not download url:{row[target_url_colum]} \n {e}")


def cli():
    parser = OptionParser()

    parser.add_option("-f", "--file", dest="file_path")
    parser.add_option("-o", "--out", dest="out_path", default="./images")
    parser.add_option("-p", "--prefix", dest="prefix", default="")
    parser.add_option("-t", "--target-url-col", dest="target_url_colum", type="int")
    parser.add_option("-n", "--name-col", dest="name_colum", default=0, type="int")
    parser.add_option("--sleep", dest="sleep", default=1, type="int")
    parser.add_option(
        "--header-skip", dest="header_skip", action="store_true", default=False
    )

    option, args = parser.parse_args()
    main(
        file_path=option.file_path,
        out_path=option.out_path,
        name_colum=option.name_colum,
        target_url_colum=option.target_url_colum,
        sleep_time=option.sleep,
        prefix=option.prefix,
        header_skip=option.header_skip,
    )
