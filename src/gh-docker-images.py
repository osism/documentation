import github
 
gh = github.Github()
 
for repository in [x for x in gh.get_organization("osism").get_repos() if x.full_name.startswith("osism/docker") and not x.archived and not "template" in x.full_name and "kolla-docker" not in x.full_name]:
    print("%s %s osism/%s" % (repository.full_name.ljust(40), repository.html_url.ljust(60), repository.full_name[14:]))
