#!/usr/bin/env python3

import yaml
from jinja2 import Template

main_template_file = "templates/index.j2.html"
main_file = "index.html"
episodes_data_file = "config/episodes.yaml"
platforms_data_tile = "config/platforms.yaml"

with open(main_template_file, "r", encoding="utf-8") as fh:
    main_template_html = fh.read()
with open(episodes_data_file, "r", encoding="utf-8") as fh:
    episodes = yaml.safe_load(fh)
    episodes.reverse()
with open(platforms_data_tile, "r", encoding="utf-8") as fh:
    platforms = yaml.safe_load(fh)

template = Template(main_template_html)
rendered_html = template.render(episodes=episodes, platforms=platforms)

with open(main_file, "w", encoding="utf-8") as fh:
    fh.write(rendered_html)
