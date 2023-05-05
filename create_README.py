import json

import jinja2

def load_user_info():
    json_open = open('user_info.json', 'r')
    json_load = json.load(json_open)
    repositories = {}
    for pull_requests_edge in json_load['user']['pullRequests']['edges']:
        repository = pull_requests_edge['node']['repository']
        if repository['owner']['login'] != 'masa-orca':
            if not repository['name'] in repositories.keys():
                repositories[repository['name']] = {}
            if not pull_requests_edge['node']['state'] in repositories[repository['name']].keys():
                 repositories[repository['name']][pull_requests_edge['node']['state']] = 1
            else:
                 repositories[pull_requests_edge['node']['repository']['name']][pull_requests_edge['node']['state']] += 1
    return {'repositories': repositories}

params = load_user_info()

env = jinja2.Environment(loader=jinja2.FileSystemLoader('./', encoding='utf8'))
template = env.get_template('README.md.j2')

rendered_result = template.render(params)
with open("README.md", "w") as o:
    o.write(rendered_result)
