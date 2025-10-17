#!/usr/bin/env python3

import os
import markdown
import shutil
import yaml
from jinja2 import Environment
from slugify import slugify

main_template_file = "templates/index.j2.html"
episode_template_file = "templates/episode.j2.html"
tag_template_file = "templates/tag.j2.html"
config_data_file = "config/config.yaml"
episodes_data_file = "config/episodes.yaml"
platforms_data_tile = "config/platforms.yaml"

if os.path.exists("episodes"):
    shutil.rmtree("episodes")
if os.path.exists("tags"):
    shutil.rmtree("tags")

with open(main_template_file, "r", encoding="utf-8") as fh:
    main_template_html = fh.read()
with open(episode_template_file, "r", encoding="utf-8") as fh:
    episode_template_html = fh.read()
with open(tag_template_file, "r", encoding="utf-8") as fh:
    tag_template_html = fh.read()
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

# Jinja environment
env = Environment()
env.filters["slugify"] = slugify

# Main page
main_template = env.from_string(main_template_html)
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
os.makedirs("episodes", exist_ok=True)
episode_template = env.from_string(episode_template_html)
for episode in episodes:
    if not episode["published"]:
        continue

    # Transcript
    transcript_file = f"transcripts/episode-{episode['id']}.md"
    transcript = None
    if os.path.exists(transcript_file):
        with open(transcript_file, "r") as fh:
            transcript = markdown.markdown(fh.read())

    # Find related episodes
    related_ids = []
    related = []
    for tag in episode["tags"]:
        if tag not in config["tags"]:
            print(
                f"WARNING: tag {tag} in episode {episode['id']} is not in the primary list"
            )
        for related_id in tags[tag]:
            if related_id == episode["id"]:
                # Skip same episode
                continue
            if related_id not in related_ids:
                related_ids.append(related_id)
                for related_episode in episodes:
                    if related_episode["id"] == related_id:
                        related.append(related_episode)

    episode_html = episode_template.render(
        config=config,
        episode=episode,
        platforms=platforms,
        related=related,
        transcript=transcript,
    )

    with open(f"episodes/episode-{episode['id']}.html", "w", encoding="utf-8") as fh:
        fh.write(episode_html)

# Tags
os.makedirs("tags", exist_ok=True)
tag_template = env.from_string(tag_template_html)
for tag, related_ids in tags.items():
    slug = slugify(tag)

    # Find related episodes
    related = []
    for related_episode in episodes:
        if related_episode["id"] in related_ids:
            related.append(related_episode)

    tag_html = tag_template.render(config=config, tag=tag, related=related)
    with open(f"tags/tag-{slug}.html", "w", encoding="utf-8") as fh:
        fh.write(tag_html)

# Update config files
with open("config/config.yaml", "w", encoding="utf-8") as fh:
    yaml.dump(
        config,
        fh,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=True,
        indent=2,
    )
with open("config/episodes.yaml", "w", encoding="utf-8") as fh:
    yaml.dump(
        episodes,
        fh,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=True,
        indent=2,
    )
