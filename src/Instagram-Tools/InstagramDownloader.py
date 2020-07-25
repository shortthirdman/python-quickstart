import argparse
import os
import requests
import time
import urllib.request
from colorama import init, deinit
from termcolor import cprint

def print_in_color(text, color):
    """ Prints `text` in passed `color` """
    cprint(text, color)

def image_downloader(edge, images_path):
    """ Downloads images """
    display_url = edge['node']['display_url']
    file_name = edge['node']['taken_at_timestamp']
    download_path = f"{images_path}\\{file_name}.jpg"
    if not os.path.exists(download_path):
        print_in_color(f"Downloading {str(file_name)}.jpg...........", "yellow")
        urllib.request.urlretrieve(display_url, download_path)
        print_in_color(f"{file_name}.jpg downloaded.\n", "green")
    else:
        print_in_color(f"{file_name}.jpg has been downloaded already.\n", "green")

def video_downloader(shortcode, videos_path):
    """ Downloads videos """
    videos = requests.get(f"https://www.instagram.com/p/{shortcode}/?__a=1")
    video_url = videos.json()['graphql']['shortcode_media']['video_url']
    file_name = videos.json()['graphql']['shortcode_media']['taken_at_timestamp']
    download_path = f"{videos_path}\\{file_name}.mp4"
    if not os.path.exists(download_path):
        print_in_color(f"Downloading {file_name}.mp4...........", "yellow")
        urllib.request.urlretrieve(video_url, download_path)
        print_in_color(f"{file_name}.mp4 downloaded.\n", "green")
    else:
        print_in_color(f"{file_name}.mp4 has been downloaded already.\n", "green")

def sidecar_downloader(shortcode, images_path, videos_path):
    """ Downloads images and videos from posts containing more than one pictures or videos """
    r = requests.get(f"https://www.instagram.com/p/{shortcode}/?__a=1")
    num = 1
    for edge in r.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:
        is_video = edge['node']['is_video']
        if not is_video:
            display_url = edge['node']['display_url']
            file_name = r.json()['graphql']['shortcode_media']['taken_at_timestamp']
            download_path = f"{images_path}\\{file_name}_{num}.jpg"
            if not os.path.exists(download_path):
                print_in_color(f"Downloading {file_name}_{num}.jpg...........", "yellow")
                urllib.request.urlretrieve(display_url, download_path)
                print_in_color(f"{file_name}_{num}.jpg downloaded.\n", "green")
            else:
                print_in_color(f"{file_name}_{num}.jpg has been downloaded already.\n", "green")
        else:
            video_url = edge['node']['video_url']
            file_name = r.json()['graphql']['shortcode_media']['taken_at_timestamp']
            download_path = f"{videos_path}\\{file_name}_{num}.mp4"
            if not os.path.exists(download_path):
                print_in_color(f"Downloading {file_name}_{num}.mp4...........", "yellow")
                urllib.request.urlretrieve(video_url, download_path)
                print_in_color(f"{file_name}_{num}.mp4 downloaded.\n", "green")
            else:
                print_in_color(f"{file_name}_{num}.mp4 has been downloaded already.\n", "green")
        num += 1

def main(account_json_info, path):
    """ Runs methods that download photos/videos from the user """
    init()
    r = requests.get(account_json_info)
    user_id = r.json()['graphql']['user']['id']
    end_cursor = ''
    next_page = True
    images_path = f"{path}\\Images"
    videos_path = f"{path}\\Videos"
    if not os.path.exists(path):
        os.makedirs(path)
        if not os.path.exists(images_path):
            os.makedirs(images_path)
        if not os.path.exists(videos_path):
            os.makedirs(videos_path)
        print_in_color("User Folder Created!\n", "magenta")
    else:
        print_in_color("User Folder Has Been Created Already!\n", "magenta")

    while next_page:
        r = requests.get('https://www.instagram.com/graphql/query/',
                params={
                    'query_id': '17880160963012870',
                    'id': user_id,
                    'first': 12,
                    'after': end_cursor
                }
            )
        graphql = r.json()['data']
        for edge in graphql['user']['edge_owner_to_timeline_media']['edges']:
            __typename = edge['node']['__typename']
            if __typename == 'GraphImage':
                image_downloader(edge, images_path)
            elif __typename == 'GraphVideo':
                shortcode = edge['node']['shortcode']
                video_downloader(shortcode, videos_path)
            elif __typename == 'GraphSidecar':
                shortcode = edge['node']['shortcode']
                sidecar_downloader(shortcode, images_path, videos_path)

        end_cursor = graphql['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        next_page = graphql['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
        time.sleep(10)
    deinit()

if __name__ == '__main__':
    print('\n\n')
    init(autoreset=True)
    print_in_color('Instagram Media Downloader'.center(os.get_terminal_size().columns, '-'), "cyan")
    deinit()

    PARSER = argparse.ArgumentParser(description='Download Instagram Images and Videos from a User\'s Profile Page')
    PARSER.add_argument('-u', '--user', dest='username', required=True, help='Username on Instagram')
    PARSER.add_argument('-p', '--path', dest='path', required=True, help='Root path where downloaded Instagram Media is saved')
    ARGS = PARSER.parse_args()

    #Insert username into link
    ACCOUNT_JSON_INFO = f"https://www.instagram.com/{ARGS.username}/?__a=1"
    ARGS.path += f"\\{ARGS.username}"
    main(ACCOUNT_JSON_INFO, ARGS.path)