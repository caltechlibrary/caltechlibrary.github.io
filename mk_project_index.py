#!/usr/bin/python3

import sys
import os
import requests
import time

version = 'v0.0.0'

def usage(app_name):
    return f'''% {app_name}(1) user manual
% R. S. Doiel
% 2022-11-16

# NAME

{app_name}

# SYNOPSIS

{app_name} [OPTIONS] GITHUB_ORGANIZATION OUTPUT_FILENAME

# DESCRIPTION

{app_name} queries the GitHub API for listing public repositories then uses their
pages API to list project repositories that have implemented pages for documentation.
{app_name} then outputs a Markdown document holding the resulting index. I can also
generate an sitemap.xml

The GITHUB_ORGANIZATION is the name of the user or organization that
you're trying to build the index for.

# OPTIONS

-h, -help, --help
: display this help

-version
: display version info

# EXAMPLE

Generate a markdown index page for "caltechlibrary" organization.

```
    {app_name} caltechlibrary
```

# REFERENCE LINKS

- [GitHub Public Repositories](https://docs.github.com/en/rest/repos/repos#list-public-repositories)
- [GitHub Pages API](https://docs.github.com/en/rest/pages)

'''

def mk_project_index(org_name, url_prefix, out_name):
    app_name = os.path.basename(sys.argv[0])
    if org_name == '':
        return 'organization name was an empty string'
    if url_prefix == '':
        return  'missing url prefix'
    if out_name == '':
        return 'missing output filename'
    page_no = 1
    projects = []
    ok = True
    u = f'https://api.github.com/orgs/{org_name}/repos'
    headers = { 'Content-Type': 'application/json', 'User-Agent': 'requests' }
    while ok:
        params = { 'type': 'public', 'sort': 'full_name', 'page': page_no }
        resp = requests.get(u, params = params, headers = headers)
        if resp.status_code == requests.codes.ok:
            try:
                data = resp.json()
            except err:
                return '', err
            if ("has_pages" in data) and data["has_pages"]:
                repo_name = repo['name']
                print(f'DEBUG inspecting data for {repo_name}', file =sys.stderr)
                if not repo_name.startswith(url_prefix.lstrip('https://')):
                    print(f'DEBUG {repo_name} has pages', file=sys.stderr)
                    projects.append(repo_name)
            page_no += 1
            # Wait 5 seconds before next request, rate limit is one a second
            time.sleep(5)
        else:
            print(f'{resp.status_code} -> reason {resp.reason}')
            ok = False

    if len(projects) > 0:
        projects.sort()
        page = ['''
Projects
========

''']
        for repo_name in projects:
            page.append(f'- [{repo_name}](./{repo_name}/)')
        with open(out_name, 'w') as f:
            f.write('\n'.join(page))
        return None
    else:
        return 'No repositories found'

if __name__ == '__main__':
    app_name = os.path.basename(sys.argv[0])
    show_help, show_version = False, False
    options = []
    for i, arg in enumerate(sys.argv):
        if arg.startswith('-'):
            if arg in [ '-h', '-help', '--help' ]:
                show_help = True
            elif arg in [ '-version' ]:
                show_version = True
            else:
                print(f'ERROR unsuppoted option ({i}) {arg}', file=sys.stderr)
                sys.exit(1)
        elif i > 0:
            options.append(arg)
    if show_help:
        print(usage(app_name))
        sys.exit(0)
    if show_version:
        print(f'{app_name} {version}')
        sys.exit(0)
    
    if len(options) != 2:
        print(f'Missing GitHub organization name or output filename, see {app_name} -help')
        sys.exit(1)
    org_name, out_name = options[0], options[1]
    err = mk_project_index(org_name, f'https://{org_name}.github.io/', out_name)
    if err != None:
        print(f'ERROR: {err}')
        sys.exit(1)
    