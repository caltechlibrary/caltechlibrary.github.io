#!/usr/bin/env python3
import sys
import os
import requests
import time
import logging as log
from datetime import datetime

log.basicConfig(encoding='utf-8', level=log.INFO)
request_delay = 15
version = 'v0.0.1'

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

def mk_project_index(org_name, url_prefix, out_name):
    if not org_name or not url_prefix or not out_name:
        return 'Organization name, URL prefix, and output filename are required.'

    log.info(f'Checking {org_name} using URL prefix {url_prefix}, output to {out_name}')
    projects = []
    page_no = 1
    continue_requests = True
    current_year = datetime.now().year
    stale_year = current_year - 4

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'requests',
        'X-GitHub-Api-Version': '2022-11-28',
        'Accept': 'application/vnd.github+json'
    }

    while continue_requests:
        params = {'type': 'public', 'sort': 'full_name', 'page': page_no}
        log.info(f'Requesting page {page_no}')

        response = requests.get(
            f'https://api.github.com/orgs/{org_name}/repos',
            params=params,
            headers=headers
        )

        if response.status_code == requests.codes.ok:
            data = response.json()

            if data:
                for repo in data:
                    repo_name = repo['name']
                    if (not url_prefix.startswith(f'https://{repo_name}') and
                        repo.get("has_pages", False) and
                        not repo.get('archived', False)):

                        if repo['pushed_at'] and int(repo['pushed_at'][:4]) >= stale_year:
                            description = repo.get('description', '')
                            if description:
                                projects.append({"name": repo_name, "description": description})
                            else:
                                log.debug(f'Skipping {repo_name}, description is incomplete')
                        else:
                            log.debug(f'Skipping {repo_name}, last active {repo["pushed_at"][:4]}')
                    else:
                        log.debug(f'Skipping {repo_name}, does not meet criteria')

                page_no += 1
                log.info(f'Waiting {request_delay} seconds before next request...')
                time.sleep(request_delay)
            else:
                continue_requests = False
        else:
            log.error(f'Error: {response.status_code} - {response.reason}')
            sys.exit(1)

    if projects:
        projects.sort(key=lambda x: x["name"])
        with open(out_name, 'w') as file:
            file.write(f'''# GitHub Projects {stale_year} through {current_year}

''')
            for repo in projects:
                file.write(f'- [{repo["name"]}](./{repo["name"]}/) - {repo["description"]}\n')
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
