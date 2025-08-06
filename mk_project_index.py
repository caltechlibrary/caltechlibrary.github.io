#!/usr/bin/env python3
import sys
import os
import requests
import time
import logging as log
from datetime import datetime, timedelta

log.basicConfig(encoding='utf-8', level=log.INFO)
version = 'v0.0.1'

def calculate_request_delay(headers):
    remaining = int(headers.get('X-RateLimit-Remaining', 5000))
    reset_timestamp = int(headers.get('X-RateLimit-Reset', time.time() + 3600))
    limit = int(headers.get('X-RateLimit-Limit', 5000))

    reset_in = max(reset_timestamp - time.time(), 1)

    if remaining < limit / 5:
        request_delay = max(reset_in / remaining, 15) if remaining > 0 else max(reset_in, 15)
    else:
        request_delay = max(15, 1)

    return request_delay

def check_rate_limit(headers):
    remaining = int(headers.get('X-RateLimit-Remaining', 0))
    limit = int(headers.get('X-RateLimit-Limit', 0))
    reset_timestamp = int(headers.get('X-RateLimit-Reset', 0))
    reset_datetime = datetime.fromtimestamp(reset_timestamp)

    log.info(f'Rate limit remaining: {remaining}/{limit}')
    log.info(f'Rate limit resets at: {reset_datetime}')

    if remaining < 1:
        sleep_time = max(reset_timestamp - time.time(), 15) + 5
        wake_up_time = datetime.now() + timedelta(seconds=sleep_time)
        log.info(f'Rate limit reached. Sleeping for {sleep_time} seconds. Will wake up at {wake_up_time}.')
        time.sleep(sleep_time)

def is_website_available(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException as e:
        log.debug(f"Website check failed for {url}: {e}")
        return False

def usage(app_name):
    help_text = f'''Usage: {app_name} [OPTIONS] GITHUB_ORGANIZATION OUTPUT_FILENAME

Generate a markdown index of GitHub repositories for a given organization.

Options:
  -h, -help, --help  Show this help message and exit.
  -version            Show version information.

Example:
  {app_name} caltechlibrary index.md
'''
    return help_text

def check_initial_rate_limit(org_name, headers):
    response = requests.head(f'https://api.github.com/orgs/{org_name}/repos', headers=headers)
    reset_timestamp = int(response.headers.get('X-RateLimit-Reset', 0))
    reset_in = reset_timestamp - time.time()

    if reset_in > 3600:
        reset_datetime = datetime.fromtimestamp(reset_timestamp)
        log.error(f'Rate limit reset is more than an hour away. Please run the program again after {reset_datetime}.')
        sys.exit(1)

def mk_project_index(org_name, url_prefix, out_name):
    if not org_name or not url_prefix or not out_name:
        return 'Organization name, URL prefix, and output filename are required.'

    log.info(f'Checking {org_name} using URL prefix {url_prefix}, output to {out_name}')
    projects = []
    page_no = 1
    continue_requests = True
    current_year = datetime.now().year
    stale_year = current_year - 4
    failure_count = 0

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'requests',
        'X-GitHub-Api-Version': '2022-11-28',
        'Accept': 'application/vnd.github+json'
    }

    check_initial_rate_limit(org_name, headers)

    while continue_requests:
        params = {'type': 'public', 'sort': 'full_name', 'page': page_no}
        log.info(f'Requesting page {page_no}')

        response = requests.get(
            f'https://api.github.com/orgs/{org_name}/repos',
            params=params,
            headers=headers
        )

        if response.status_code == requests.codes.ok:
            failure_count = 0
            check_rate_limit(response.headers)
            request_delay = calculate_request_delay(response.headers)

            data = response.json()

            if data:
                for repo in data:
                    repo_name = repo['name']

                    if repo.get('archived', False):
                        log.debug(f'Skipping {repo_name}, repository is archived')
                        continue

                    if not repo.get('has_pages', False):
                        log.debug(f'Skipping {repo_name}, repository does not have GitHub Pages enabled')
                        continue

                    if repo['pushed_at'] and int(repo['pushed_at'][:4]) < stale_year:
                        log.debug(f'Skipping {repo_name}, last active {repo["pushed_at"][:4]}')
                        continue

                    description = repo.get('description', '')
                    if not description:
                        log.debug(f'Skipping {repo_name}, description is incomplete')
                        continue

                    website_url = f"{url_prefix}{repo_name}/"
                    if is_website_available(website_url):
                        projects.append({"name": repo_name, "description": description})
                    else:
                        log.debug(f'Skipping {repo_name}, website is not available')

                page_no += 1
                log.info(f'Waiting {request_delay} seconds before next request...')
                time.sleep(request_delay)
            else:
                continue_requests = False
        else:
            failure_count += 1
            log.error(f'Error: {response.status_code} - {response.reason}')
            if failure_count >= 10:
                log.error('Too many failures. Exiting.')
                sys.exit(1)
            check_initial_rate_limit(org_name, headers)
            sleep_time = 15
            wake_up_time = datetime.now() + timedelta(seconds=sleep_time)
            log.info(f'Failure {failure_count}/10. Sleeping for {sleep_time} seconds. Will wake up at {wake_up_time}.')
            time.sleep(sleep_time)

    if projects:
        projects.sort(key=lambda x: x["name"])
        with open(out_name, 'w') as file:
            file.write(f'''# GitHub Projects {stale_year} through {current_year}

''')
            for repo in projects:
                file.write(f'- [{repo["name"]}]({url_prefix}{repo["name"]}/) - {repo["description"]}\n')
    else:
        return 'No repositories found'

if __name__ == '__main__':
    app_name = os.path.basename(sys.argv[0])
    if '-h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
        print(usage(app_name))
        sys.exit(0)
    if '-version' in sys.argv:
        print(f'{app_name} {version}')
        sys.exit(0)

    if len(sys.argv) != 3:
        print(f'Usage: {app_name} GITHUB_ORGANIZATION OUTPUT_FILENAME')
        sys.exit(1)

    org_name, out_name = sys.argv[1], sys.argv[2]
    error = mk_project_index(org_name, f'https://{org_name}.github.io/', out_name)
    if error:
        print(f'Error: {error}')
        sys.exit(1)
