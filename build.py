#!/usr/bin/env python3

import yaml
from jinja2 import Template

main_template_file = "templates/index.j2.html"
episode_template_file = "templates/episode.j2.html"
config_data_file = "config/config.yaml"
episodes_data_file = "config/episodes.yaml"
platforms_data_tile = "config/platforms.yaml"

with open(main_template_file, "r", encoding="utf-8") as fh:
    main_template_html = fh.read()
with open(episode_template_file, "r", encoding="utf-8") as fh:
    episode_template_html = fh.read()
with open(config_data_file, "r", encoding="utf-8") as fh:
    config = yaml.safe_load(fh)
with open(episodes_data_file, "r", encoding="utf-8") as fh:
    episodes = []
    for episode in yaml.safe_load(fh):
        if episode["published"]:
            episodes.append(episode)
    episodes.reverse()
with open(platforms_data_tile, "r", encoding="utf-8") as fh:
    platforms = yaml.safe_load(fh)


# Main page
main_template = Template(main_template_html)
main_html = main_template.render(config=config, episodes=episodes, platforms=platforms)

with open("index.html", "w", encoding="utf-8") as fh:
    fh.write(main_html)


# Read tags
tags = {}
for episode in episodes:
    if not episode["published"]:
        continue
    for tag in episode["tags"]:
        if tag not in tags:
            tags[tag] = []
        tags[tag].append(episode["id"])


# Per episode page
episode_template = Template(episode_template_html)
for episode in episodes:
    if not episode["published"]:
        continue

    # Find related episodes
    related_ids =[]
    related = []
    for tag in episode["tags"]:
        for related_id in tags[tag]:
            if related_id == episode["id"]:
                # Skip same episode
                continue
            if related_id not in related_ids:
                related_ids.append(related_id)
                for related_episode in episodes:
                    if related_episode["id"] == related_id:
                        related.append(related_episode)

    episode_html = episode_template.render(config=config, episode=episode, platforms=platforms, related=related)
    with open(f"episodes/episode-{episode['id']}.html", "w", encoding="utf-8") as fh:
        fh.write(episode_html)
