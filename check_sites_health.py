import argparse
from datetime import datetime
import requests
import whois


def load_urls4check(path):
    with open(path) as urls_file:
        for url in urls_file:
            yield url.strip()


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.status_code == requests.codes.ok


def get_domain_expiration_date(domain_name):
    domain_info = whois.whois(domain_name)
    expiry_date = domain_info.expiration_date
    if isinstance(expiry_date, list):
        return expiry_date[0]
    return expiry_date


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='path of file with urls')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_arguments()
    path_to_file_with_urls = args.filepath
    urls_for_check = load_urls4check(path_to_file_with_urls)
    for url in urls_for_check:
        print(url)
        print('\tHTTP response status is 200:',
              'ok' if is_server_respond_with_200(url) else 'False'
              )
        expiry_date = get_domain_expiration_date(url)
        if expiry_date:
            prepaid_period = (expiry_date - datetime.now()).days
            print('\tDomain prepaid one month ahead:', end=' ')
            if prepaid_period > 30:
                print('ok')
            else:
                print('NO. Domain expires {}'.format(expiry_date))
        else:
            print('\tExpiry date cannot be evaluated.\n')
